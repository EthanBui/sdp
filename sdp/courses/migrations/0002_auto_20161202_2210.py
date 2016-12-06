# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocomponent',
            name='contentType',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='date_completed',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filecomponent',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagecomponent',
            name='content',
            field=models.TextField(),
        ),
    ]
