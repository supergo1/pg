from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
