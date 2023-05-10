from django.urls import path
from . import views

app_name = 'entry_app'

urlpatterns = [
    path('', entry_app.views.signin_view, name='signin'),
    path('signup/', entry_app.views.signup_view, name='signup'),

]
