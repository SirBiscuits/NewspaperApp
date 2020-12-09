from django.contrib import admin
from django.urls import path, include
from register import views as v
from . import settings
from django.contrib.auth.views import (
    LoginView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include ("newspaperApp.urls")),
    path('', include ("django.contrib.auth.urls")),
]

