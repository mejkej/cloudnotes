from django.urls import path
from . import views

app_name = 'entry_app'

urlpatterns = [
    path('', views.entry_view, name='entry'),
]
