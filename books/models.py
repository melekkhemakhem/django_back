from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=165)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class Upload(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    url = models.ImageField(upload_to='uploads/')
class Student(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    fee = models.IntegerField()