from django.db import models
from django import forms
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to = "images/")
    completed = models.BooleanField(default=False)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

class Meta:
    db_table = "myapp_image"
# AUTOMOBILE_CHOICES = [
#     ('Bus', 'Bus'),
#     ('Car', 'Car'),
#     ('Auto', 'Auto'),
#     ('Bike', 'Bike'),
#     ]
# class Automobiles(models.Model):
# #     Automobiles = models.CharField(max_length=100, choices = AUTOMOBILE_CHOICES, default='Bus')
#     Automobiles = forms.ChoiceField(required=False, widget = forms.CheckboxSelectMultiple, choices = AUTOMOBILE_CHOICES)

    def _str_(self):
        return self.title