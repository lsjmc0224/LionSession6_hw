from django.shortcuts import render
from django.contrib.auth.models import User

def mypage(request):
    return render(request,'users/mypage.html')