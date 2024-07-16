from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
fio = 'Пескова А.О.'
name = 'Александра'
secname = 'Олеговна'
surname = 'Пескова'
phone = '8-9**-211-31-18'
email= 'peskoval**@gmail.com'


items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    text = f'''
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{fio}</i>
    '''
    return HttpResponse(text)


def about(request):
    text = f'''
    Имя: {name}<br>
    Отчество: {secname}<br>
    Фамилия: {surname}<br>
    телефон: {phone}<br>
    email: {email}'''
    return HttpResponse(text)


def all_items(request):
    list_items = [item['name'] for item in items]
    page = f'''
    <html><head><title>list of all items</title></head>
    <body>{list_items[0]}<br>
    {list_items[1]}<br>
    {list_items[2]}<br>
    {list_items[3]}<br>
    {list_items[4]}
    </body>
    </html>
    '''
    return HttpResponse(page)