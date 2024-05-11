from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class  Meta:
        model=Task
        fields={'title','description','important'}  
        Widgets={
            'title':forms.TextInput(attrs={'class':'form-control ' }),
            'description':forms.Textarea(attrs={'class':'form-control '}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input text-center'}),
        }