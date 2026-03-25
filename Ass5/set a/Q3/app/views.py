from django.shortcuts import render,redirect
def home(request): return render(request,'home.html')
def second(request): return render(request,'second.html')
def redirect_page(request): return redirect('second')