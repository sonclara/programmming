#models==module!!!-하나의 파이썬 파일
from django.db import models
from django import forms
import re
from django.core.validators import RegexValidator
from programmming.utils import random_name_upload_to


# Create your models here. (모듈.클래스-상속이란 얘기지!!!)
#뭐가 문제니?????? 돌지말자~
def min_length_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하세요')

def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    return RegexValidator(r'^01[016789]\d{7,8}$',
        message = '휴대폰번호를 입력하세요! 이상한 거 넣지마요!')(number)

class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(phone_validator)


class Post(models.Model):

    title = models.CharField(max_length=100,
        validators=[min_length_validator],
        help_text='포스팅 제목을 100자 이내로 써주세요.')
    content = models.TextField()
    category = models.ForeignKey('Category',)
    photo = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    phone = PhoneField(blank=True)
    tags =models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    email = models.EmailField(max_length=254, null=True)
    message= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.message


class Tag(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.category


class Guest_book(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, null=True)
    content = models.TextField()
    photo = models.ImageField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.name
