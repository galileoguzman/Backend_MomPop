from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recipe(models.Model):
    """
    Custom user class.
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/recipes', default='uploads/default.jpg')


    def __unicode__(self):
        return self.title