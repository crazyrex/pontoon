# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-31 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0076_auto_20170104_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='branch',
            field=models.CharField(blank=True, max_length=2000, verbose_name=b'Branch'),
        ),
    ]