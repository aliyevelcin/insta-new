from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.hashers import make_password
from django.views.generic import   DetailView, CreateView  
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
 
from core.forms import CommentForm
from core.models import Comment, Post
from accounts.forms import ThePasswordChangeForm, ResetPasswordConfirmForm, ResetPasswordForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class ProfileView(DetailView ,FormMixin):
    model = User
    template_name = "profile.html"
    form_class = CommentForm
    context_object_name = "user"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('accounts:profile_account', args=[self.kwargs['slug']])

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.account = self.request.user
        post = Post.objects.get(pk=int(self.request.POST['post']))
        form.instance.account_post = post
        form.save()
        return super().form_valid(form)

class RegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')


 
class LoginUserView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

 
class UpdatePasswordView(PasswordChangeView):
    template_name = 'update.html'
    form_class = ThePasswordChangeForm
    success_url = reverse_lazy('accounts:login')


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'


class ResetPasswordView(PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name= "password_reset_confirm.html" 
    success_url = reverse_lazy('accounts:login')

