from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage),
    path('home/', views.homepage, name='home'),
    path('accounts/login/', views.loginPage, name='login'),
    path('accounts/signup/', views.signupUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('<str:short_code>/', views.newUrl, name='redirect_to_new'),

]
