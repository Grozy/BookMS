#-*- coding:utf-8 –*-

from django.db import models
from django.contrib import admin
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(u'书名', default="",max_length=150)
    book_create_time = models.DateField('购书日期')
    book_logo_url = models.CharField('图片地址', default="", max_length=150)

class BookBorrow(models.Model):
    book_id = models.IntegerField()
    is_borrowed = models.BooleanField('图书借阅状态', default=False)
    book_borrowed_time = models.DateField('被借阅日期')

class UserBaseInfo(models.Model):
    # no = models.AutoField()
    name = models.CharField("昵称",default="",max_length=16)
    uid = models.IntegerField("员工编号") #公司的工号
    account = models.CharField("用户名",default="",max_length=30)
    password = models.CharField("密码", default="", max_length=16)
    avator_url = models.TextField("头像",null=False, blank=True)

class UserTypeInfo(models.Model):
    uid = models.IntegerField("员工编号")
    user_type = models.CharField("用户类型", default="", max_length=1)

class BorrowHistory(models.Model):
    book_id = models.IntegerField("图书编号")
    uid = models.IntegerField("员工编号")
    borrow_time = models.DateField("借阅日期")
    is_over_time = models.BooleanField("是否越期",default=False)

class BookList(admin.ModelAdmin):
    list_display = ("book_name", "book_create_time")

class UserList(admin.ModelAdmin):
    list_display = ("name", "account", "password")

admin.site.register(Book, BookList)
admin.site.register(UserBaseInfo, UserList)
admin.site.register(UserTypeInfo)
admin.site.register(BorrowHistory)