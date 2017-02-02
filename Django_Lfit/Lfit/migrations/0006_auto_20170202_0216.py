# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lfit', '0005_auto_20170126_2123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='latestcycles',
            new_name='CycleCreate',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='method',
        ),
        migrations.AddField(
            model_name='compresults',
            name='complocation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='compresults',
            name='compname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compresults',
            name='dl1',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='compresults',
            name='dl2',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='compresults',
            name='dl3',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='paymentmethod',
            field=models.CharField(choices=[('cash', 'Cash'), ('pp', 'Paypal'), ('bank', 'Bank Transfer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='compresults',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='affiliatedivision',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=50, null=True),
        ),
    ]