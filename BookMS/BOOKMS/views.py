#-*- coding:utf-8 –*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from BOOKMS.models import Book

CONSTDBPATH = '../../db.sqlite3'

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def login(request):
    return render_to_response("login.html")

def bookFetch(request):
    bookFetchResult = Book.objects.get(book_title = u'代码重构')
    print('%s',bookFetchResult.book_title)
    html = "<html><body>In hour(s), it will be.</body></html>"
    return render_to_response(html)