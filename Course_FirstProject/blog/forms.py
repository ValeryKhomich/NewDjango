from django import forms


class UserForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()