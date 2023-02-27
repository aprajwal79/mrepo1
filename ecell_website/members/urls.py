from django.urls import path
from . import views

urlpatterns = [
    # int:numbers
    # str:strings
    # path:whole urls/
    # slug:hyphen-and_underscores...
    # UUID:universally unique identifier
    path('login_user', views.login_user, name="login"),
]
