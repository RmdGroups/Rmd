from django.db import models


class Musician(models.Model):
    idno=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=100)
class Album(models.Model):
    idno = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
