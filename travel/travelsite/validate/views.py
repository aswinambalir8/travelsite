from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method== 'POST':
        usr = request.POST['username']
        pas = request.POST['password']
        val = auth.authenticate(username=usr,password=pas)
        if val is not None:
            auth.login(request,val)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    return render(request,'login.html')
# Create your views here.
def register(request):
    if request.method== 'POST':
        user = request.POST['username']
        first = request.POST['first_name']
        last = request.POST['last_name']
        mail = request.POST['email']
        fpass = request.POST['password']
        cpass = request.POST['password1']
        if fpass == cpass:
            if User.objects.filter(username=user).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,'email already registered')
                return redirect('register')
            else:
                aut = User.objects.create_user(username=user,first_name=first,last_name=last,email=mail,password=fpass)
                aut.save();
                return redirect('login')


        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')