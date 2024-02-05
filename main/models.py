from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(first_name)

