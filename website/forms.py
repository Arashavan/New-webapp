from django import forms
from website.models import Contact


# class NameForm(forms.Form):
#     Name = forms.CharField(label="Name", max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=225)
#     message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
