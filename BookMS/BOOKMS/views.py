#-*- coding:utf-8 –*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from BOOKMS.models import Book
import json

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def login(request):
    return render_to_response("login.html")

# def bookFetch(request):
#     bookFetchResult = Book.objects.all()
#     html = "<html><body>%s</body></html>"
#     content = ""
#     for book in bookFetchResult:
#         content = content + (u"<p>书名是%s.录入日期为%s</p>"%(book.book_title,book.createTime))
#     return HttpResponse(html%content)

def booklist(request):
    response_data = {}
    page = request.GET.get('page')
    size = request.GET.get('size')
    book_fetch = Book.objects.all()
    book_info_list = []
    for book in book_fetch:
        book_info = {}
        book_info['book_name'] = book.book_name
        book_info['create_time'] = book.book_create_time.datetime
        book_info_list.append(book_info)

    print(book_info_list)
    return HttpResponse(json.dumps(book_info_list))