#-*- coding:utf-8 –*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from BOOKMS.models import Book
from BOOKMS.models import UserBaseInfo

import json

# Create your views here.
def hello(request):
    print(request.path)
    print(request.get_host())
    print(request.get_full_path())
    print(request.is_secure())
    # print(request.META)
    try:
        ua = request.META['aaa']
    except KeyError:
        ua = 'unknow'
    print(ua)
    return HttpResponse("Hello world")
    # render_to_response('search.html')

def search(request):
    print('%s' % (request.GET['q']))

    return render_to_response('search.html')

def login(request):
    return render_to_response("login.html")

# def bookFetch(request):
#     bookFetchResult = Book.objects.all()
#     html = "<html><body>%s</body></html>"
#     content = ""
#     for book in bookFetchResult:
#         content = content + (u"<p>书名是%s.录入日期为%s</p>"%(book.book_title,book.createTime))
#     return HttpResponse(html%content)

def register(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    avator_url = request.GET.get('avator')
    account = request.GET.get('account')
    userId = request.GET.get('user_id')

    userInfo = UserBaseInfo(user_id = userId,user_name = name,user_password = password, user_account = account, user_avator_url = avator_url)
    userInfo.save()
    data = {}
    data['state'] = True
    return HttpResponse(json.dump(data))

def booklist(request):
    page = request.GET.get('page')
    size = request.GET.get('size')
    book_fetch = Book.objects.all()
    book_info_list = []
    for book in book_fetch:
        book_info = {}
        book_info['book_name'] = book.book_name
        book_info['create_time'] = "%s" % book.book_create_time
        book_info['author'] = book.book_author
        book_info['book_icon'] = book.book_logo_url
        book_info['description'] = book.book_description
        book_info_list.append(book_info)
        print(book)
    return HttpResponse(json.dumps(book_info_list))
