from django.db import models

# Create your models here.

class todo(models.Model):
    task=models.CharField(max_length=50)


class product(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    imageUrl=models.CharField(max_length=200)
