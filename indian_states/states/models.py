
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    language = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.name
