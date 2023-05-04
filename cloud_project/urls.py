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
from entry_app.views import user_signin, user_signup, not_authenticated, user_logout
from main_app.views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_signin, name='user_signin'),
    path('signup/', user_signup, name='user_signup'),
    path('main/', main_page, name='main_page'),
    path('logout/', user_logout, name='user_logout'),

]
