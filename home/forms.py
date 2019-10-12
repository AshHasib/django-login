from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')


class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name (e.g. John Doe)'}), label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username (e.g. john123)'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label='')
    profile_pic = forms.ImageField(label='Upload profile picture:')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype password'}), label='')

    