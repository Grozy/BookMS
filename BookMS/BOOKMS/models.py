#-*- coding:utf-8 –*-

from django.db import models
from django.contrib import admin
# Create your models here.

class Book(models.Model):
    book_title = models.CharField('书名',max_length=150)
    book_borrow_status = models.BooleanField('图书借阅状态',default=False)
    createTime = models.DateField('购书日期')

class BookList(admin.ModelAdmin):
    list_display = ("book_title", "createTime")

class User(models.Model):
    user_name = models.CharField('姓名',max_length=150)
    user_id = models.CharField('工号',max_length=6)
    user_department = models.CharField('部门',max_length=150)
    user_password = models.CharField('密码',max_length=10)

class UserList(admin.ModelAdmin):
    list_display = ("user_name", "user_id", "user_department")

admin.site.register(Book, BookList)
admin.site.register(User, UserList)
