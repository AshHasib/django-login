from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}), label='')


class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label='')
    profile_pic = forms.ImageField(label='Upload profile picture:')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}), label='')
    re_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')