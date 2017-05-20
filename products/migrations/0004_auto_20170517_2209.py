# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
