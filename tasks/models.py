from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=49)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.title
