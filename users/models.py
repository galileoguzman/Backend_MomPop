from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    """
    Custom user class.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('email address', unique=True, db_index=True)
    type_user = models.BooleanField(default=True)
    born_date = models.DateField(auto_now=False, auto_now_add=False)
    avatar = models.ImageField(upload_to='uploads', default='uploads/default.jpg')
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

