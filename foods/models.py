from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Food(models.Model):
    """
    Custom user class.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/foods', default='uploads/default.jpg')
    qtc = models.IntegerField()


    def __unicode__(self):
        return self.name