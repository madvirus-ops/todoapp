from django.shortcuts import render
from .forms import RegisterForm, UserProfileForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            new_user.save()
            
            return render(request, 'user/login.html',)

    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})       