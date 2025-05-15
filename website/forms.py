from django import forms


class Nameform(forms.Form):
    Name = forms.CharField(label="Name", max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=225)
    message = forms.CharField(widget=forms.Textarea)
