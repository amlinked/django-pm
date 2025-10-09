from . import models
from django import forms

attrs = {"class" : "form-control"}
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ("category","title","description")
        widgets = {
            'category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs)
        }


class ProjectUpdateForm(forms.ModelForm):   
    class Meta:
        model = models.Project
        fields = ("category","title","description", "status")
        widgets = {
            'category' : forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs),
            'status':forms.Select(attrs=attrs)
            
        }
