from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        
        else:
            return render(request,'accounts/login.html')     
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')


def signup(request):
    #POST요청이 들어오면
    if request.method == 'POST':
        #password와 confirm에 써있는 값이 같은지 확인
        if request.POST['password'] == request.POST['confirm']:
            #user를 만든다. username과 password는 각각 사용자가 입력한 값을 준다.
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
                
                )
            
            nickname=request.POST['nickname']
            department=request.POST['department']
            
            profile = Profile(user=user, nickname=nickname, department=department)
            profile.save()
            #로그인시킨다.
            auth.login(request,user)
            return redirect('/')
    return render(request, 'accounts/signup.html')