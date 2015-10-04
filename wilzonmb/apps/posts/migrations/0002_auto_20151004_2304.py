# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='web',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
