from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شماره تلفن  خود را وارد کنید'}),
        required = False
    )
    adress1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس1 خود را وارد کنید'}),
        required = False
    )
    adress2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس 2 خود را وارد کنید'}),
        required = False
    )
    city =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' شهر خود را وارد کنید'}),
        required = False
    )
    state =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شهرستان خود را وارد کنید'}),
        required = False
    )
    zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '  کد پستی خود را وارد کنید'}),
        required = False
    )
    country =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' کشور  خود را وارد کنید'}),
        required = False
    )
    class Meta:
        model = Profile
        fields = ('phone','adress1','adress2','city','state','zipcode','country')

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','name':'password', 'type': 'password', 'placeholder': 'رمز خود را وارد کنید'})
    )
    new_password2 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','name':'password', 'type': 'password', 'placeholder': 'رمز خود را وارد کنید'})
    )
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

class UpdateUserForm(UserChangeForm):
    password=None
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام خانوادگی  خود را وارد کنید'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ایمیل  خود را وارد کنید'})
    )
    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام کاربری'})

    )

    class Meta:
        model = User
        fields= ('first_name', 'last_name', 'email', 'username', )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام خانوادگی  خود را وارد کنید'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ایمیل  خود را وارد کنید'})
    )
    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام کاربری'})

    )
    password1 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','name':'password', 'type': 'password', 'placeholder': 'رمز خود را وارد کنید'})
    )
    password2 = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class':'form-control','name':'password', 'type': 'password', 'placeholder': 'رمز خود را وارد کنید'})
    )
    class Meta:
        model = User
        fields= ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')