from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('wrrr')
                else:
                    return HttpResponse('Konto jest Zablokowane')
            else:
                return HttpResponse('Nieprawidłowe hasło lub login')
    else:
        form = LoginForm()
    return  render(request, 'account/login.html', {'form':form})

