from django.shortcuts import render

from .forms import HomeForm
from .utils import get_users, save_users


template_name = 'mainApp/homePage.html'

def index(request):
    form = HomeForm()
    return render(request, template_name, {'form': form})


def save_random_users(request):
    """Функция сохраняет в БД первых 5 пользователей 
       с сайта 'https://randomuser.me, у которых в имени
       и фамилии нет буквы 'R'.

    """
    form = HomeForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        result = save_users(form.cleaned_data['n_users'])
        if not result['success']:
            return {'form': form, 'error_message': result['reasons']}

        args = {'form': form, 'count': result['count']}
        return render(request, template_name, args)

    return render(request, template_name, {'form': form, 'error_message': 'ERROR'})


def show_users(request):
    """Функции отображает всех пользователей из БД"""
    
    form = HomeForm()
    args = {'form': form, 'random_users': get_users()}
    return render(request, template_name, args)
