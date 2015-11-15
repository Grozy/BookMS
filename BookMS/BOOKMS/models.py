#-*- coding:utf-8 –*-

from django.db import models
from django.contrib import admin
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(u'书名', default="",max_length=150)
    book_create_time = models.DateField('购书日期')
    book_logo_url = models.CharField('图片地址', default="", null=False, max_length=150) #书的封面图标
    book_author = models.CharField('作者',max_length=30)  #作者的姓名
    book_ISBN = models.CharField('ISBN',max_length=13)  #ISBN十三位
    book_paper_type = models.CharField('纸质',max_length=10)
    book_description = models.TextField('内容简介')

    def __unicode__(self):
        return self.book_name

class UserBaseInfo(models.Model):
    # no = models.AutoField()
    user_name = models.CharField("昵称",default="",max_length=16)
    user_id = models.IntegerField("员工编号",unique=True) #公司的工号
    user_account = models.CharField("用户名",default="",max_length=30)
    user_password = models.CharField("密码", default="", max_length=16)
    user_avator_url = models.TextField("头像",null=False, blank=True)

class BookBorrow(models.Model):
    book = models.ForeignKey(Book)
    borrow_by_user = models.ForeignKey(UserBaseInfo)
    is_borrowed = models.BooleanField('图书借阅状态', default=False)
    book_borrowed_time = models.DateField('被借阅日期')

class UserTypeInfo(models.Model):
    user = models.ForeignKey(UserBaseInfo)
    user_type = models.CharField("用户类型", default="", max_length=1)

class BorrowHistory(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(UserBaseInfo)
    borrow_time = models.DateField("借阅日期")
    is_over_time = models.BooleanField("是否越期",default=False)

class BookList(admin.ModelAdmin):
    list_display = ("book_name", "book_create_time")

class UserList(admin.ModelAdmin):
    list_display = ("user_name", "user_account", "user_password")

class BorrowHistoryDisplay(admin.ModelAdmin):
    list_display = ("book", "user", "borrow_time")

admin.site.register(Book, BookList)
admin.site.register(UserBaseInfo, UserList)
admin.site.register(UserTypeInfo)
admin.site.register(BorrowHistory, BorrowHistoryDisplay)