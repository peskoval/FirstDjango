
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item

# Create your views here.


# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }

    return render(request, "about.html", {"author": author})


def get_item(request, item_id):
    """ По указанному id возвращает элемент из списка. """
    try:
        if Item.ojectbs.get(pk=item_id):
            context = {
                "item": Item.objects.get(pk=item_id)
            }
        return render(request, 'item.html', context)
    except AttributeError:
        return HttpResponseNotFound(f"Товар с id={item_id} не найден")


def get_items(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items.html", context)
       
