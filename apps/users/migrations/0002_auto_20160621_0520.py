# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='uploads/default.jpg', upload_to='uploads/avatars'),
        ),
    ]
