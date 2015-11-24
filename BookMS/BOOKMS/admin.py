#-*- coding:utf-8 –*-

from django.contrib import admin
from models import Book,UserBaseInfo,BookBorrow,BorrowHistory

# Register your models here.

# book_name = models.CharField(u'书名', default="",max_length=150)
#     book_create_time = models.DateField('购书日期')
#     book_logo_url = models.CharField('图片地址', default="", null=False, max_length=150) #书的封面图标
#     book_author = models.CharField('作者',max_length=30)  #作者的姓名
#     book_ISBN = models.CharField('ISBN',max_length=13)  #ISBN十三位
#     book_paper_type = models.CharField('纸质',max_length=10)
#     book_description = models.TextField('内容简介')
class BookList(admin.ModelAdmin):
    list_display = ("book_name", "book_create_time")
    search_fields = ("book_name", "book_create_time")#搜索
    list_filter = ('book_create_time',)#时间进行过滤  今天、昨天、本周、本月、本年~
    # filter_horizontal = ('book_name') check box
class UserList(admin.ModelAdmin):
    list_display = ("user_name", "user_account", "user_password")#列表页显示的数据

class BorrowHistoryDisplay(admin.ModelAdmin):
    list_display = ("book", "user", "borrow_time")
    ordering = ("-borrow_time",)#根据借阅时间排序

admin.site.register(Book, BookList)
admin.site.register(UserBaseInfo, UserList)
admin.site.register(BorrowHistory, BorrowHistoryDisplay)
