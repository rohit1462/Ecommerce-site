from django.shortcuts import render
from django.views import View

# Create your views here.


class BasePage(View):
    def get(self, request):
        return render(request, 'base.html')
    
class SignInPage(View):
    def get(self,request):
        return render(request,'signin.html')

def signUpPage(request):
    return render(request, 'signup.html')
