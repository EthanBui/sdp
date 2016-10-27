# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('contentType', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('isPublished', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCompleted', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequenceNumber', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Module'),
        ),
    ]