from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm, NewsForm, Product


def ProductView(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        country = request.POST.get("country")
        city = request.POST.get("city")
        street = request.POST.get("street")
        apartment = request.POST.get("apartment")
        number_house = request.POST.get("number_house")
        return HttpResponse(f'{name} {surname}, проверьте адрес доставки: <br>'
                            f'{country} <br>'
                            f'{city} <br>'
                            f'{street} <br>'
                            f'{number_house} <br>'
                            f'{apartment} <br>')
    else:
        form = Product()
    return render(request, 'dilivery.html', context={'form':form})

def shop(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f'User {name}, Age {age}')
    else:
        form = UserForm()
    return render(request, 'shop.html', context={'form':form})

def myForm(request):
    return render(request, 'form.html')
# def user(request):
#     name = request.POST.get("name")
#     age = request.POST.get("age")
#     return HttpResponse(f'User {name}, Age {age}')


def NewsView(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_publisher = request.POST.get("is_publisher")
        category = request.POST.get("category")
        return HttpResponse(f'Новость {title} <br>'
                            f'Контент: {content} <br>'
                            f'Категория {category}, {is_publisher}')
    else:
        form = NewsForm()
    return render(request, 'news.html', context={'form':form})
