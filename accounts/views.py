from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('livro:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            print(dir(form))
            user = form.save()
            login(request, user)
            return redirect('livro:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_views(request):
    logout(request)
    return redirect('livro:index')
