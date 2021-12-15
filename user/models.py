from django.db import models

# Create your models here.
class Decent(models.Model):
    decent_id = models.IntegerField(max_length=10,primary_key='true')
    decent_name = models.CharField(max_length=50)
class User (models.Model):
    user_id= models.IntegerField(max_length=10, primary_key='true')
    user_mail = models.CharField(max_length=50, default='')
    user_pass = models.CharField(max_length=50, default='')
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=10)
    decent = models.ForeignKey(Decent, on_delete=models.CASCADE)