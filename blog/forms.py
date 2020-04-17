from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=25)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Wprowadź email"}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Wprowadź email"}))
    comments = forms.CharField(required=False, widget = forms.Textarea(attrs={"class": "form-control","rows": 3}))
    