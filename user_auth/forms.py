from django import forms


class UserForm(forms.Form):
    user_name = forms.CharField(required=True, max_length=100)
    age = forms.IntegerField(
        required=True,
        min_value=18,
    )
    email = forms.EmailField(required=True, max_length=100)
    password = forms.CharField(required=True, max_length=256)
