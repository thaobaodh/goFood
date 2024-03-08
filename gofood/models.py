from django.db import models

# Create your models here.

class Book_Table(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Number = models.IntegerField(max_length=20)
    Date = models.DateField()
    Person = models.IntegerField(max_length=10)