from django.shortcuts import render
from .models import Food
# Create your views here.

def index(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'myapp/index.html', context)