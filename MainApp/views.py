from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


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
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={item_id} не найден")
    else:
        context = {"item": item}
        return render(request, 'item_page.html', context)
    


def get_items(request):
    # Получить все элементы из таблицы MainApp_item
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)
       