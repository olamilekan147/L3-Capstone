from django.urls import path
from band.views import home, members, events, login_user, authenticate_user, reg_user, logout_user


urlpatterns = [
    path('', home, name='home'),
    path('members/', members, name='members'),
    path('events/', events, name='events'),
    path('login/', login_user, name='login'),
    path("auth_user/", authenticate_user, name="auth_user"),
    path("reg_user/", reg_user, name='reg_user'),
    path("logout/", logout_user, name='logout')
]