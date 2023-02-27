from django.urls import path
from . import views

urlpatterns = [
    # int:numbers
    # str:strings
    # path:whole urls/
    # slug:hyphen-and_underscores...
    # UUID:universally unique identifier
    path('', views.home, name="home"),
    path('startup/', views.startup, name="startup"),
    path('events/', views.events, name="events"),
    path('members/', views.members, name="members"),
    path('gallery/', views.gallery, name="gallery"),
]

