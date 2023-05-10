from django.urls import path
from . import views

app_name = 'entry_app'

urlpatterns = [
    path('', signin_view, name='signin'),
    
]
