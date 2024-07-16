from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

author = {
    "Имя": "Александра",
    "Отчество": "Олеговна",
    "Фамилия": "Пескова",
    "телефон": "8-9**-211-31-18",
    "email": "peskoval**@gmail.com"
}

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
    Имя: {author["Имя"]}<br>
    Отчество: {author["Отчество"]}<br>
    Фамилия: {author["Фамилия"]}<br>
    телефон: {author['телефон']}<br>
    email: {author["email"]}
    """
    return HttpResponse(text)


def get_item(request, item_id):
    """ По указанному id возвращает элемент из списка. """
    for item in items:
        if item['id'] == item_id:
            context = {
                "title": item['name'],
                "name": item['name'],
                "quantity" : item['quantity'],
        }
        return render(request, "item.html", context)
    return HttpResponseNotFound(f"Товар с id={item_id} не найден")


def get_items(request):
    context = {
        "items": [item['id'], item['name'], item['quantity']],
    }
    return render(request, "items.html", context)
       