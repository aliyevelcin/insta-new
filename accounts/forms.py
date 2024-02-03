from django import forms 
from accounts.models import User 
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm

class ThePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Cari şifrənizi daxil edin',
                'class' : 'text',
            }))

    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Yeni şifrənizi daxil edin',
                'class' : 'text',
            }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Yeni şifrənizi yenidən daxil edin',
                'class' : 'text',
            }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifre',
                'class' : 'login-input',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifreni tekrarla',
                'class' : 'login-input',
            }))

    email = forms.EmailField(
            widget = forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'login-input',
            })
        )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Kullanıcı adı', 'class': 'login-input'}),
            'first_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'Adı Soyadı', 'class': 'login-input'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'login-input',
        'placeholder': 'Username',
        'name': 'username'
    }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'login-input',
            'name': 'password',
            'placeholder': 'Password'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password']



class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'login-input',
        })
    )

class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'login-input',
             }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password again',
                'class' : 'login-input',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )