from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# from socialproject.users.forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):

    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse("User authenticated and Logged-In")
            else:
                return HttpResponse("Invalid Login")

    else:
        form=LoginForm()
    return render(request, 'users/login.html', {'form':form} )

# django checks the password verification if it's present in backend does by ORM

@login_required
def index(request):
    return render(request, 'users/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')