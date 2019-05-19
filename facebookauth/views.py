from django.shortcuts import render
from django.contrib.auth import logout as logout_user
from django.http import HttpResponse
from django.views import View

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout_user(request)
        return render(request, 'logout.html')