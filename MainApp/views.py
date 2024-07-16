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
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Пескова А.О.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: {author["Имя"]}<br>
    Отчество: {author["Отчество"]}<br>
    Фамилия: {author["Фамилия"]}<br>
    телефон: {author['телефон']}<br>
    email: {author["email"]}
    """
    return HttpResponse(text)


# /item/1 
# /item/2
# ...
# /item/n
def get_item(request, item_id):
    """ По указанному id возвращает элемент из списка. """
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Имя: {item['name']} </h2>
            <p> Количество: {item['quantity']} </p>
            <p> <a href='/items'>Назад к списку товаров</a> </p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Товар с id={item_id} не найден")


def get_items(request):
    result = "<h1> Список товаров </h1><ol>" 
    for item in items:
        result += f"""<li><a href='/item/{item["id"]}'> {item["name"]} </a></li>"""
    result += "</ol>"
    return HttpResponse(result)
       