# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lfit', '0017_auto_20170217_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]