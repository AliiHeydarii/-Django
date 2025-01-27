from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser , Profile
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'گذرواژه'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'تکرار گذرواژه'})


    class Meta:
        model = CustomUser
        fields = ("email", 'username' , 'phone_number', 'password1' , 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'شماره همراه'}),
        }

    
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not data.isnumeric():
            raise ValidationError('شماره همراه باید عددی باشد')
        return data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", 'username' , 'phone_number')
        


class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name' , 'last_name' , 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }