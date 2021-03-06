# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lfit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('first', models.CharField(max_length=50, null=True)),
                ('last', models.CharField(max_length=50, null=True)),
                ('cycle', models.CharField(max_length=50, null=True)),
                ('payplan', models.IntegerField(choices=[('12', '12'), ('14', '14')], null=True)),
                ('weeks', models.IntegerField(null=True)),
                ('totaltopay', models.IntegerField(null=True)),
                ('paid', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=50, null=True)),
                ('method', models.CharField(choices=[('cash', 'cash'), ('pp', 'paypal'), ('bank', 'bank transfer')], max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='compresults',
            name='weightclass',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
