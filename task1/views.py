from django.shortcuts import render
from .forms import UserRegister
from .models import *

# Create your views here.
def platform(request):
    return render(request, 'platform.html')


def games_view(request):
    Games = Game.objects.all()
    context = {
        "Games": Games
    }
    return render(request, 'games.html', context)

def cart_view(request):
    return render(request, 'cart.html')

def sign_up(request):
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, password=password, age=age)
                info['success'] = f'Приветствуем, {username}!'

    info['form'] = form
    return render(request, 'registration_page.html', info)