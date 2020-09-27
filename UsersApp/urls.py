from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'users'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('google/', TemplateView.as_view(template_name="users/google.html")),
]
