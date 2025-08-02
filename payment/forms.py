from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'نام کامل  خود را وارد کنید'}),
        required = False
    )
    shipping_phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شماره تلفن  خود را وارد کنید'}),
        required = False
    )
    shipping_email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شماره email  خود را وارد کنید'}),
        required = False
    )
    shipping_adress1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس1 خود را وارد کنید'}),
        required = False
    )
    shipping_adress2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس 2 خود را وارد کنید'}),
        required = False
    )
    shipping_city =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' شهر خود را وارد کنید'}),
        required = False
    )
    shipping_state =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شهرستان خود را وارد کنید'}),
        required = False
    )
    shipping_zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '  کد پستی خود را وارد کنید'}),
        required = False
    )
    shipping_country =  forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' کشور  خود را وارد کنید'}),
        required = False
    )
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name','shipping_phone','shipping_email','shipping_adress1','shipping_adress2','shipping_city','shipping_state','shipping_zipcode','shipping_country']
        exclude= ['user',]
