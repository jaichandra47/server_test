from django import forms

class RegisterForm(forms.ModelForm):
    first_name = forms.TextField()
    last_name = forms.TextField()
    user_name = forms.TextField()
    email_id = forms.TextField()
    phone_number = forms.IntegerField()