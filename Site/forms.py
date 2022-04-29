from django import forms
from datetime import date
from .models import M_Mouse, K_Keyboard, H_HeadSet
from django.contrib.auth.models import User
from django.forms import ModelForm


class ManufacturerForm(forms.Form):
    Manufacturer_name = forms.CharField(label="Название бренда")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}), }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class MouseForm(forms.ModelForm):
    class Meta:
        model = M_Mouse
        fields = '__all__'
        widgets = {
            'M_Mouse_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'M_Mouse_Manufacturer': forms.Select(attrs={'class': 'form-control', 'id': 'manufact'}),
            'M_Mouse_ConnectType': forms.Select(attrs={'class': 'form-control', 'id': 'type'}),
            'M_Mouse_Frequency': forms.Select(attrs={'class': 'form-control', 'id': 'freq'}),
            'M_Mouse_DPI': forms.Select(attrs={'class': 'form-control', 'id': 'dpi'}),
            'M_Mouse_ConnectionInt': forms.Select(attrs={'class': 'form-control', 'id': 'cint'}),
            'M_Mouse_Image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}),
            'M_Mouse_Price': forms.NumberInput(attrs={'class': 'form-control', 'value': '5000', 'id': 'price'}),
            'M_Mouse_SenserModel': forms.Select(attrs={'class': 'form-control', 'id': 'sens'}),
        }


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = K_Keyboard
        fields = '__all__'
        widgets = {
            'K_Keyboard_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'K_Keyboard_Manufacturer': forms.Select(attrs={'class': 'form-control', 'id': 'manufact'}),
            'K_Keyboard_Type': forms.Select(attrs={'class': 'form-control', 'id': 'type'}),
            'K_Keyboard_SwitchModel': forms.Select(attrs={'class': 'form-control', 'id': 'switch'}),
            'K_Keyboard_Format': forms.Select(attrs={'class': 'form-control', 'id': 'format'}),
            'K_Keyboard_ConnectType': forms.Select(attrs={'class': 'form-control', 'id': 'cnt'}),
            'K_Keyboard_Image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}),
            'K_Keyboard_Price': forms.NumberInput(attrs={'class': 'form-control', 'value': '5000', 'id': 'price'}),
            'K_Keyboard_ConnectionInt': forms.Select(attrs={'class': 'form-control', 'id': 'cint'}),
        }


class HeadsetForm(forms.ModelForm):
    class Meta:
        model = H_HeadSet
        fields = '__all__'
        widgets = {
            'H_HeadSet_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'H_HeadSet_Manufacturer': forms.Select(attrs={'class': 'form-control', 'id': 'manufact'}),
            'H_HeadSet_Scheme': forms.Select(attrs={'class': 'form-control', 'id': 'scheme'}),
            'H_HeadSet_Hz': forms.Select(attrs={'class': 'form-control', 'id': 'hz'}),
            'H_HeadSet_Sens': forms.Select(attrs={'class': 'form-control', 'id': 'sens'}),
            'H_HeadSet_ConnectType': forms.Select(attrs={'class': 'form-control', 'id': 'cnt'}),
            'H_HeadSet_Image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}),
            'H_HeadSet_Price': forms.NumberInput(attrs={'class': 'form-control', 'value': '5000', 'id': 'price'}),
            'H_HeadSet_ConnectionInt': forms.Select(attrs={'class': 'form-control', 'id': 'cint'}),
            'H_HeadSet_Set': forms.Select(attrs={'class': 'form-control', 'id': 'set'}),
        }