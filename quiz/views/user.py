from django.shortcuts import render, redirect
from quiz.forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from quiz.models import *



def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="candidate")
            user.groups.add(group)
            messages.success(request, 'Account was created for '+ username)
            
            return redirect('login')
    context = {'form' : form}
    return render(request, 'registration/register.html', context = context)

def history(request, user_id):
    user = User.objects.get(id = user_id)
    results = Result.objects.filter(user = user).order_by('-created')
    context = {
        'results': results,
    }
    return render(request, 'account/history.html', context=context)


