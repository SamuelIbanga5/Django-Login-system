from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect



@login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')

@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f"Account has been created for {user}.")
                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username OR Password is incorrect.")

    # context = {'form': form}
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
