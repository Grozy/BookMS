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
    bookFetchResult = Book.objects.all()
    html = "<html><body>%s</body></html>"
    content = ""
    for book in bookFetchResult:
        content = content + (u"<p>书名是%s.录入日期为%s</p>"%(book.book_title,book.createTime))


    return HttpResponse(html%content)