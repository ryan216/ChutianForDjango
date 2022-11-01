from django.db import models

# Create your models here.
from django.db import models


class page1(models.Model):
    about = models.TextField(default='', null=True, blank=True)
    nums_1 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_2 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_3 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_4 = models.CharField(max_length=100,default='', null=True, blank=True)

    service1 = models.TextField(default='', null=True, blank=True)
    service2 = models.TextField(default='', null=True, blank=True)
    service3 = models.TextField(default='', null=True, blank=True)

    innovation1 = models.TextField(default='', null=True, blank=True)
    innovation2 = models.TextField(default='', null=True, blank=True)
    innovation3 = models.TextField(default='', null=True, blank=True)

    work1 = models.TextField(default='', null=True, blank=True)
    work2 = models.TextField(default='', null=True, blank=True)
    work3 = models.TextField(default='', null=True, blank=True)


class news(models.Model):
    title = models.CharField(max_length=100, default='', null=True, blank=True)
    content = models.TextField(default='', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField()
