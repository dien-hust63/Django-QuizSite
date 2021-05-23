from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class QuizTestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('extra')
        detail_result = kwargs.pop('detail_result')
        super().__init__(*args, **kwargs)
        for question in questions:
            answer_list = forms.ModelMultipleChoiceField(
                required = False,
                queryset=question.list_answer,
                widget  = forms.CheckboxSelectMultiple()
            )
            if question.technique == 0:
                self.fields[f"{question.id}"] = answer_list
            else:
                self.fields[f"{question.id}"] = forms.CharField(widget=forms.Textarea)
            self.fields[f"{question.id}"].label = question.title + ". " +question.content
            if detail_result == 1:
                self.fields[f"{question.id}"].widget.attrs.update({'disabled':'disabled'})

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ("__all__")


class QuizForm(forms.ModelForm):
    class Meta: 
        model = Quiz
        fields = ("__all__")

            
    
                                 

