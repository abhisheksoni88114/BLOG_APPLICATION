from django import forms
from .models import Comment

class Postemail(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)

class Postcomment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']