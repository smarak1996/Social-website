from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView,LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

urlpatterns = [
 #path('login/', views.user_login, name='login'),
 path('', views.dashboard, name='dashboard'),path('', views.dashboard, name='dashboard'),
 path('login/',LoginView.as_view(template_name='account/registration/login.html'),name="login"),
 path('logout/',LogoutView.as_view(template_name='account/registration/logged_out.html'),name="logout"),
 path('passwordchange/',PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),name="password_change"),
 path('passwordchangedone/',PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),name="password_change_done"),
 path('passwordreset/',PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'),name="password_reset"),
 path('passwordresetdone/',PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'),name="password_reset_done"),
 re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'),name="password_reset_confirm"),
  
 
]