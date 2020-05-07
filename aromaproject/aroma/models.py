from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Товар: {self.name} - id товара: {self.id}'


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    pages = models.PositiveIntegerField()
    format = models.CharField(max_length=64)
    publish_year = models.PositiveIntegerField()

    def __str__(self):
        return f'Название: {self.title} - Автор: {self.author}'

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return f'Название: {self.title}'