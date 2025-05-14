from django import forms


class Nameform(forms.From):
    name = forms.CharField(label="name", max_length=255)
