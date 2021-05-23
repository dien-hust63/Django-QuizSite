from django.shortcuts import render
from quiz.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login')
def index(request):
    user = request.user
    user_per = request.user.groups.first().name
    context = {'user': user}
    if( user_per == "candidate"):
        return render(request, "user_index.html",context=context)
    else:
        return render(request, "staff_index.html",context=context)