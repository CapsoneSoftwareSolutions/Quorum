from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

class Topic(models.Model):
	creator=models.ForeignKey(User)
	topic=models.CharField(max_length=250)
	created=models.DateTimeField(auto_now_add=True)
	imgurl=models.FileField(upload_to='topics', blank=True)
	desc=models.TextField()
	def __unicode__(self):		
		return unicode(self.topic)
class class1(models.Model):
	na=models.TextField()
	image=models.FileField(upload_to = 'imagefolder',blank=True)

class QuestionManager(models.Manager):
	def topicspecific_count(self, keyword):
		return self.filter(topic__pk=keyword).count()

	def get_last_question(self,keyword):
		try:
			return self.filter(topic__pk=keyword).order_by("-created")[0]
		except IndexError: return ''

class Question(models.Model):
	user=models.ForeignKey(User)
	created=models.DateTimeField(auto_now_add=True)
	topic=models.ForeignKey(Topic)
	question=models.TextField()
	tags=models.CharField(max_length=50,blank=True)
	objects = QuestionManager()
	def __unicode__(self):
		usr=self.user.username
		return u"User: %s, Question: %s" %(usr,self.question)
	def favscount(self):
		return Favourites.objects.filter(question=self).count()

class feedback(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField()
	dateofpost=models.DateTimeField(auto_now_add=True)

class FavouritesManager(models.Manager):
    def does_user_stared(self,usr,quest):
    	try: 
    		self.get(user=usr,question=quest)
    		return ("btn-primary","UnFollow")#on
    	except:
    		return ("","Follow")

class Favourites(models.Model):
    '''Does this your Favourite Question'''
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question)
    objects = FavouritesManager()

class Followings(models.Model):
	'''	Are u following this topic'''
	user=models.ForeignKey(User)
	topic=models.ForeignKey(Topic)
	def __unicode__(self):
		usr=self.user.username
		tp=self.topic.topic
		return "User: %s, Topic: %s" %(usr,tp)

class QuestionRating(models.Model):
	user=models.ForeignKey(User)#who rated
	question=models.ForeignKey(Question)
	vote=models.IntegerField(max_length=1,default=0)
	favourate=models.BooleanField(default=False)
	def __unicode__(self):
		usr=self.user.username
		quest=self.question.id
		return u"User: %s, Question ID: %d" %(usr,quest)

class Answer(models.Model):
	user=models.ForeignKey(User)
	created=models.DateTimeField(auto_now_add=True)
	question=models.ForeignKey(Question)
	answer=models.TextField()
	correct=models.BooleanField(default=False)
	def __unicode__(self):
		usr=self.user.username
		quest=self.question.id
		return u"User: %s,  Question ID: %d" %(usr,quest)

	def save(self, *args, **kwargs):
		"""Email when a answer is added."""
		if "notify" in kwargs and kwargs["notify"] == True and self.user.email:
			message = "An Answer was added to '%s' by '%s': \n\nQuestion:\n%s" % (self.question.topic.topic, kwargs["ans"],
                                                                         self.question)
			#from_addr = EMAIL_HOST_USER
			#recipient_list = [self.user.email,]
			send_mail("New answer added", message, 'no-replay@itechtalents.com', kwargs["mailing_list"])

		if "notify" in kwargs: del kwargs["notify"]
		if "ans" in kwargs: del kwargs["ans"]
		if "mailing_list" in kwargs: del kwargs["mailing_list"]
		super(Answer, self).save(*args, **kwargs)

class AnswerRating(models.Model):
	'''
	Answer can be rated by any user,
	but the correct answer is only selected by
	the question user'''

	user=models.ForeignKey(User)#who rated the answer
	answer=models.ForeignKey(Answer)
	vote=models.IntegerField(max_length=1,default=0)
	favourate=models.BooleanField(default=False)
	def __unicode__(self):
		usr=self.user.username
		quest=self.answer.question.id
		return u"User: %s, Question ID: %d" %(usr,quest)

admin.site.register(Topic)
#admin.site.register(Question)
#admin.site.register(QuestionRating)
#admin.site.register(Answer)
#admin.site.register(AnswerRating)
#admin.site.register(Favourites)
#admin.site.register(Followings)