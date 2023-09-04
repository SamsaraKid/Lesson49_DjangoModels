from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=10)
    age = forms.IntegerField(min_value=0, max_value=120)