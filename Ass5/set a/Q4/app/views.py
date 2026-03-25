from django.shortcuts import render
from django.contrib.auth import authenticate,login
def home(request): return render(request,'home.html')
def login_view(request):
    error=None
    if request.method=='POST':
        user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            login(request,user)
            return render(request,'success.html',{'user':user})
        else:
            error='Invalid Username or Password'
    return render(request,'login.html',{'error':error})