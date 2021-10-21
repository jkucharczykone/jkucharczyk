from django import forms
from .models import Comment
class EmailPostForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=25)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Wprowadź email"}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Wprowadź email"}))
    comments = forms.CharField(required=False, widget = forms.Textarea(attrs={"class": "form-control","rows": 3}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=25)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Wprowadź email"}))
    body = forms.CharField(widget = forms.Textarea(attrs={"class": "form-control","rows": 6}))

class SearchForm(forms.Form):
    query = forms.CharField()
    