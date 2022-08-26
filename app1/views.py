from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userlogin
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'login.html')
def verify(request):
    username = request.POST['name']
    passcode = request.POST['passcode']
    if userlogin.objects.filter(username=username).exists():
        if(passcode == userlogin.objects.filter(username=username)[0].password):
            user=userlogin.objects.filter(username=username)[0].username
            return render(request,'profile.html',{'user':user})
        else:
            messages.info(request,'Invalid username/password')
            return redirect('/')
    else:
        messages.info(request,'Invalid username/password')
        return redirect('/')
def createacc(request):
    return render(request,'signup.html')
def verify1(request):
    username = request.POST['name']
    pass1 = request.POST['passcode']
    pass2 = request.POST['passcode1']
    if userlogin.objects.filter(username=username).exists():
        messages.info(request,"Username Already Taken")
        return redirect('/signup')
    elif pass1 != pass2:
        messages.info(request,"Passwords Dont Match")
        return redirect('/signup')
    else:
        user = userlogin.objects.create(username=username,password=pass1)
        user.save()
        return render(request,'profile1.html',{'user':username})
def about(request):
    return render(request,'about.html')
def report(request):
    return render(request,'report.html')


