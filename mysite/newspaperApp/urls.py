from django.urls import path
from django.conf.urls import include
from .views import Home, create_comment, Profile

urlpatterns = [
    # path('', views.home, name="home"), # specify names for each of our urls so we can access them easily
    path('', Home.as_view(), name="home"),
    path('comment/create/', create_comment, name="create_comment"),
    path('profile/', Profile, name="profile"),
]
