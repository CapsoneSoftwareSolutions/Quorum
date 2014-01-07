from django.forms import ModelForm,ValidationError
from quorum.models import Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field,Layout, ButtonHolder, Submit
from quorum.models import Question,Answer,Topic

class AnswerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('answer',css_class="field span8"),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-primary pull-right')
            )
        )
        super(AnswerForm, self).__init__(*args, **kwargs)
    
    def clean_answer(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'answer' in self.cleaned_data:
            if len(self.cleaned_data['answer'].strip())<20:
                raise ValidationError("Answer must have atleast 20 characters.")
        return self.cleaned_data

    class Meta:
        model = Answer
        fields=("answer",)#exclude = ["post"]



class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('topic',css_class="input-xxlarge"),
            Field('question',css_class="input-xxlarge"),
            #Field('tags',css_class="input-xxlarge"),
         #   class=
        #    ButtonHolder(
        #        Submit('submit', 'Submit', css_class='btn-primary')
        #    )
        )
        self.helper.add_input(Submit('submit', 'Post Your Question',css_class="btn-inverse"))
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
    	fields=("topic","question",)