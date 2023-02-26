from django.urls import path
from registration import views

urlpatterns = [
    path('base/', views.BasePage.as_view(), name='base'),
    path('login/',views.SignInPage.as_view(),name='login')
]
