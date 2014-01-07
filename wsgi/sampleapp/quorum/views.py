
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render#_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from quorum.models import Question,Answer,feedback,Topic,Favourites,Followings,class1
from quorum.forms import QuestionForm,AnswerForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    topics=Topic.objects.all()#.order_by("-created")    
    return render(request,"quorum/home.html", {'topics':topics})


def questions(request,pk=None):
    """Main listing."""
    tp=''
    if pk:
        top=Topic.objects.get(id=pk)
        qall=False #selected topic questions
        quests = Question.objects.filter(topic__pk=pk).order_by("-created")
        tp=top.topic
    else:
        tp='All Questions'
        qall=True #all questions       
        quests = Question.objects.all().order_by("-created")
        # for i in quests:
        #     print i
    paginator = Paginator(quests, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:quests = paginator.page(page)
    except (InvalidPage, EmptyPage):
        quests = paginator.page(paginator.num_pages)

    #favorites = Favourites.objects.filter(question=quest)
    d = dict(quests=quests,user=request.user,quest_list=quests.object_list,
        topic=tp,qall=qall)
    return render(request,"quorum/questions.html", d)

def cur_question_dict(request,pk):
    quest = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=quest)
    favorites = Favourites.objects.filter(question=quest)
    btnfollow=Favourites.objects.does_user_stared(request.user,quest)
    fav={'total':favorites.count(),'btnclass':btnfollow[0],'btntext':btnfollow[1]}
    return dict(quest=quest,ans=answers,user=request.user,fav=fav)

@csrf_exempt
def question(request, pk):
    try:qst = Question.objects.get(pk=pk)
    except:return HttpResponse("Sorry The Requested Page NotFound!")
    error=''
    if request.method == 'POST':        
        if request.POST['actiontype']=='add':            
            if len(request.POST['answer'].strip())<10:error="atleast 10 characters required."
            else:                    
                ans, created = Answer.objects.get_or_create(user=request.user,question=qst)
                if created:
                    user_answered=request.user.first_name+request.user.last_name
                    a_usr=[i.user.email for i in Answer.objects.filter(question=qst)]
                    a_usr.append(qst.user.email)
                    ans.answer=request.POST['answer']
                    ans.save(notify=False,ans=user_answered,mailing_list=a_usr)
                else:
                    error="Sorry You cannot post more than 1 answer. Please edit the current answer!"
                
        else:
            cur_ans=Answer.objects.get(user=request.user,question=qst)
            if request.POST['actiontype']=='edit':
                cur_ans.answer=request.POST['answer']
                cur_ans.save()
            elif request.POST['actiontype']=='del':
                n={'ans_pk':cur_ans.pk}
                cur_ans.delete()
                return HttpResponse(json.dumps(n), mimetype="application/json")
    d=cur_question_dict(request,pk)
    d['error']=error
    return render(request,"quorum/question.html", d) 
@login_required
def add_question(request):
    if request.method == 'POST':
        frm = QuestionForm(request.POST)
        if frm.is_valid():
            topic=Topic.objects.get(id=int(request.POST['topic']))
            qs=Question(user=request.user,topic=topic)

            frm=QuestionForm(request.POST,instance=qs)
            frm.save()            
            return HttpResponseRedirect('/quorum/question/all')
    else:
        frm=QuestionForm()
    d = dict(form=frm,user=request.user)
    d.update(csrf(request))
    return render(request,"quorum/ask.html",d)#{"form":frm})
####3new

def mark_as_favorite(request):#, question_id, *args, **kwargs):
    if request.user.is_authenticated():
        q_id=int(request.GET['param1'])
        qst=Question.objects.get(pk=q_id)
        fav, created = Favourites.objects.get_or_create(user=request.user, question=qst)
        if created:
            updated="mark"
        else:
            fav.delete()
            updated="unmark"
    else:
        updated="nouser"
        
    n={"updated": updated,}
    return HttpResponse(json.dumps(n), mimetype="application/json")


def mark_follow(request):#, question_id, *args, **kwargs):
    if request.user.is_authenticated():
        t_id=int(request.GET['param1'])
        tp=Topic.objects.get(pk=t_id)
        fav, created = Followings.objects.get_or_create(user=request.user, topic=tp)
        if created:
            updated="followed"
        else:
            fav.delete()
            updated="unfollowed"
    else:
        updated="nouser"        
    n={"updated": updated,}
    return HttpResponse(json.dumps(n), mimetype="application/json")


from django.contrib.auth.models import User
def quorumuser(request,username):
    userview=User.objects.get(username=username)
    #print userview
    if request.user.is_authenticated():usr=request.user           
    else:usr=''
    #return HttpResponse(username)    
    return render(request,"quorum/user_home.html",{"user":usr,"userview":userview})

def quorumusers(request):
    if request.user.is_authenticated():usr=request.user
    else:usr=""
    usrs=User.objects.all()
    return render(request,"quorum/users.html",{"users":usrs,"user":usr})



def save_contact_info(request):
    usr=User.objects.get(id=request.user.id)
    #print usr
    #emp_info=EmployerInfo.objects.get(employer__user=request.user)
    f_name=request.GET['param1']
    f_value=request.GET['param2']  
    #print f_name 
    setattr(usr, f_name, f_value)
    try:
        usr.save()
        updated='t'
    except: updated='f'
    n={ 
        "updated": updated,
        "fname":f_name,
        }
    return HttpResponse(json.dumps(n), mimetype="application/json")
def tasks(request):
    name=request.GET['t']
    from subprocess import call
    import os
    PROJECT_DIR=os.path.dirname(os.path.realpath(__file__))
    path=os.path.join(PROJECT_DIR,'..', 'manage.py')
    if name:
        x=call([path, name])
    
    return HttpResponse('called successfully:'+str(x))
# def txtarea(request):
#     if request.method=='POST':
#         # print "hi"
#         va=request.POST.get("desc")
#         img=request.FILES.get('img1')
#         return HttpResponse("uplaoded")
#         class1(na=va,image=img).save()
#         return HttpResponseRedirect('/txtarea')
#     else:    
#         v=class1.objects.all()
#         return render(request,"quorum/textarea.html",{'v':v})
def privacypolicy(request):
    return render(request,"quorum/privacypolicy.html")
def help(request):
    return render(request,"quorum/help.html")

def feedbacks(request):
    from django.template.loader import render_to_string
    from django.contrib.sites.models import Site
    from django.contrib import messages
    if request.method=="POST":
        current_site = Site.objects.get_current()
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        sub=request.POST.get('subject')
        feedbck=request.POST.get('feedback')
        mail=request.POST.get('email')
        usr=User.objects.get(is_staff=True)
        emsub='User feedback from %s' %current_site.domain
        ctx_dict = {'fname': fname, 'lname': lname, 'subject': sub, 'email' : mail, 'feedback' : feedbck, 'domain' : current_site.domain }
        message = render_to_string('quorum/feedback.txt',ctx_dict)
        send_mail(emsub, message, mail,[usr.email])
        feedback(firstname=request.POST['firstname'],lastname=lname,email=mail,subject=sub,message=feedbck).save()
        messages.success(request, 'Your feedback has been submited successfully')
        return HttpResponseRedirect('/feedback/')
    return render(request,"quorum/feedback.html")
