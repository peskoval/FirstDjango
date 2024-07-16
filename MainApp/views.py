from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
fio = 'Пескова А.О.'
name = 'Александра'
secname = 'Олеговна'
surname = 'Пескова'
phone = '8-9**-211-31-18'
email= 'peskoval**@gmail.com'

def home(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{fio}</i>
    """
    return HttpResponse(text)

def about(request):
    text = f'''
    Имя: {name}<br>
    Отчество: {secname}<br>
    Фамилия: {surname}<br>
    телефон: {phone}<br>
    email: {email}'''

    return HttpResponse(text)