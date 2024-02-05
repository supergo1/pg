from django.db import models


class User(models.Model):
<<<<<<< HEAD
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

=======
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
>>>>>>> 9ea37b778b75eb7cebcda92c0c47d1c03200816d
