from django.db import models

# Create your models here.
from django.db import models



class page1(models.Model):
    about= models.CharField(max_length=500,default='',null=True,blank=True)
    nums_1=models.CharField(max_length=20,default='',null=True,blank=True)
    nums_2=models.CharField(max_length=20,default='',null=True,blank=True)
    nums_3=models.CharField(max_length=20,default='',null=True,blank=True)
    nums_4=models.CharField(max_length=20,default='',null=True,blank=True)

    service1= models.CharField(max_length=500,default='',null=True,blank=True)
    service2= models.CharField(max_length=500,default='',null=True,blank=True)
    service3= models.CharField(max_length=500,default='',null=True,blank=True)

    innovation1= models.CharField(max_length=500,default='',null=True,blank=True)
    innovation2= models.CharField(max_length=500,default='',null=True,blank=True)
    innovation3= models.CharField(max_length=500,default='',null=True,blank=True)

    work1= models.CharField(max_length=500,default='',null=True,blank=True)
    work2= models.CharField(max_length=500,default='',null=True,blank=True)
    work3= models.CharField(max_length=500,default='',null=True,blank=True)





