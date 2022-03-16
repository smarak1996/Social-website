from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView, PasswordChangeView, PasswordChangeDoneView 

urlpatterns = [
 #path('login/', views.user_login, name='login'),
 path('', views.dashboard, name='dashboard'),path('', views.dashboard, name='dashboard'),
 path('login/',LoginView.as_view(template_name='account/registration/login.html'),name="login"),
 path('logout/',LogoutView.as_view(template_name='account/registration/logged_out.html'),name="logout"),
 path('passwordchange/',PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),name="password_change"),
 path('passwordchangedone/',PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),name="password_change_done"),
    
 
]