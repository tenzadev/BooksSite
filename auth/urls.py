from django.urls import path
from .views import register_user, logout_user, login_user

urlpatterns = [
    path('login/', login_user, name="login_user"),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name="logout_user")
]
