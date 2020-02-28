from django.db import models


class Usuario(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=12, default=" ")
    position = models.IntegerField(default=0)