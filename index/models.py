from django.db import models

# Create your models here.
from django.db import models

class page1(models.Model):
    about = models.TextField(default='',null=True,blank=True)
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

    title = models.CharField(max_length=100,default='',null=True,blank=True)
    header = models.CharField(max_length=100,default='',null=True,blank=True)
    type = models.CharField(max_length=100,default='',null=True,blank=True)
    content = models.TextField(default='',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)



class about(models.Model):
    introduction = models.TextField(default='',null=True,blank=True)
    progress = models.TextField(default='',null=True,blank=True)
    nums_1 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_2 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_3 = models.CharField(max_length=100,default='', null=True, blank=True)
    nums_4 = models.CharField(max_length=100,default='', null=True, blank=True)

    d1_name= models.CharField(max_length=100,default='', null=True, blank=True)
    d2_name= models.CharField(max_length=100,default='', null=True, blank=True)
    d3_name= models.CharField(max_length=100,default='', null=True, blank=True)
    d4_name= models.CharField(max_length=100,default='', null=True, blank=True)

    d1_content= models.TextField(default='',null=True,blank=True)
    d2_content= models.TextField(default='',null=True,blank=True)
    d3_content= models.TextField(default='',null=True,blank=True)
    d4_content= models.TextField(default='',null=True,blank=True)





class department(models.Model):
    name= models.CharField(max_length=100,default='', null=True, blank=True)
    introduction = models.TextField(default='', null=True, blank=True)
    about = models.ForeignKey("about",on_delete=models.CASCADE)


class service(models.Model):
    title = models.CharField(max_length=100,default='',null=True,blank=True)
    header = models.CharField(max_length=100,default='',null=True,blank=True)
    type = models.CharField(max_length=100,default='',null=True,blank=True)
    content = models.TextField(default='',null=True,blank=True)


class pm_con(models.Model):
    content = models.TextField(default='',null=True,blank=True)