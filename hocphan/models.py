from django.db import models

# Create your models here.
# table Khoa
class Majors(models.Model):
    major_id=models.IntegerField(max_length=10, primary_key='true')
    major_name = models.CharField(max_length=100)
# table hoc phan
class Subjects(models.Model):
    sub_id=models.IntegerField(max_length=10, primary_key='true')
    sub_name=models.CharField(max_length=100)
    major=models.ForeignKey(Majors, on_delete=models.CASCADE)
# table documents
class Docs(models.Model):
    doc_id = models.IntegerField(max_length=10, primary_key='true')
    doc_name = models.CharField(max_length=100)
    sub=models.ForeignKey(Subjects, on_delete=models.CASCADE)
