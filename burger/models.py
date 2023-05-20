from django.db import models

class MyModel(models.Model):
    photo = models.ImageField(upload_to='photos/')