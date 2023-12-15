from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully')
            return redirect ('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information are incorrect')
                return redirect ('login')
    else:
        form = AuthenticationForm()
    return render (request,'register.html',{'form':form,'type':'Login'})

@login_required
def profile(request):
    return render(request,'profile.html')


def user_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('homepage')

@login_required
def pass_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(user=request.user,data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request,pass_form.user)
            messages.success(request,'Password updated successfully')
            return redirect('homepage')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':pass_form})

@login_required
def pass_change2(request):
    if request.method == 'POST':
        pass_form = SetPasswordForm(user=request.user,data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request,pass_form.user)
            messages.success(request,'Password updated successfully')
            return redirect('homepage')
    else:
        pass_form = SetPasswordForm(user=request.user)
    return render(request,'pass_change.html',{'form':pass_form})
            