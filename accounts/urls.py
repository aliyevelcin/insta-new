from django.urls import path
from accounts.views import  ProfileView ,RegisterView,LoginUserView, UpdatePasswordView, ForgetPasswordView, ResetPasswordView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'


urlpatterns = [
    path('profile/<slug:slug>',ProfileView.as_view(),name ='profile_account'),
    path('register/',RegisterView.as_view(),name ='register'),
    path('login/',LoginUserView.as_view(),name ='login'),
    path('log-out', LogoutView.as_view(), name='log-out'),
    path('change-password/', UpdatePasswordView.as_view(), name='change-password'),
    path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name = 'password-reset-confirm'),
]