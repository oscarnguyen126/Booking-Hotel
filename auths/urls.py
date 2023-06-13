from django.urls import path
from auths import views


urlpatterns = [
    path("login/", views.login_page),
    path("logout/", views.logout_page),
]
