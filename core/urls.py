from django.urls import path
from core.views import app

urlpatterns = [
    path('application/', app, name='application')
]
