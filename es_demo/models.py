from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    birthday = models.DateField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.username
