
from django.urls import path
from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='user-register'),
    path('login/', user_views.loginUser, name='user-login'),
    path('logout/', user_views.logoutUser, name='user-logout'),
]