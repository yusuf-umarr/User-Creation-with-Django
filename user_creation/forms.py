from django import forms
from django.contrib.auth.models import User


from .models import user_data

class singup_form(forms.ModelForm):
    
    email                 = forms.EmailField()
    password              = forms.CharField(widget=forms.PasswordInput())
    confirm_password      = forms.CharField(widget=forms.PasswordInput())
        

    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password', 'confirm_password')

    def clean(self):
        cleaned_data = super(singup_form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError ("password does not match")

    def clean_username(self):
        if User.objects.filter(email=self.cleaned_data['username']).exists():
            raise forms.ValidationError("username taken")
        return self.cleaned_data['username']


    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("email already exist")
        return self.cleaned_data['email']