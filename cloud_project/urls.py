"""CLOUD_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from entry_app.views import entry_page
from main_app.views import main_page, log_out


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entry_page, name='entry_app/entry.html'),
    path('main/', main_page, name='main_app/main.html'),
    path('', log_out, name='entry_app/logout'),


]
