from django.shortcuts import render
from napp import forms

# Create your views here.
def home(request):
    return render(request,'napp/home.html')

def register(request):
    if request.method=="POST":
        password=request.POST.get('password')
        userform=forms.UserRegistration(request.POST)
        if userform.is_valid():
            user=userform.save(commit=False)
            user.set_password(password)
            user.save()
    form=forms.UserRegistration()
    return render(request,'napp/register.html',{'form':form})
