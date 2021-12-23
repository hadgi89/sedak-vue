from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user, login, logout, authenticate
from django.contrib import messages

from .forms import UserLoginForm, UserCreationForm


def sign_in (request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login (request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'account/auth-signin.html', {'form': form})



def sign_out(request):
    logout(request)
    return redirect('signin')


# def sign_up (request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Ви успішно зареєструвалися')
#             return redirect('signin')
#         else:
#             messages.error(request, 'Помилка при реєстрації')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/auth-signup.html', {'form': form})

#! Можно сразу при регистрации пользователя его авторизировать
def sign_up (request):
    pass
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'account/auth-signup.html', {'form': form})

    
    
    
    
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST) # создаем объект формы и заполняем данными из POST
    #     if form.is_valid(): # валидация - если форма валидна, то ...
    #         form.save() # сохраняем форму
    #         messages.success(request, 'Ви успішно зареєструвалися')
    #         return redirect('auth_signin')
    #     else:
    #         messages.error(request, 'Помилка при реєстрації')
    # else:
    #     form = UserCreationForm() # не связанная форма
    # return render(request, 'users/auth-signup.html', {'form': form})
    

    # return render(request, 'users/auth-signup.html', {'form': form})  # путь к шаблону + передача формы в контекст 
    
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         # #после валидации данные формы попадают в словарь cleaned_data, из которого эти данные мы можем сохранить
    #         # CustomUser.objects.create(**form.cleaned_data) # '**' - расспаковка словаря в python
    #         return redirect('auth_signin')

    #         # или перенаправление на созданный объект:
    #         # user = CustomUser.objects.create(**form.cleaned_data)
    #         # return redirect(user)
    # else:
    #     form = CustomUserCreationForm()
    # return render(request, 'users/auth-signup2.html') 