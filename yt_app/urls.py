from django.urls import path
from .views import *

app_name = 'yt_app'

urlpatterns = [
    path('', home_view, name='home')
]