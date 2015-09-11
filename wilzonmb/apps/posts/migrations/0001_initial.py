# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description_short', ckeditor.fields.RichTextField()),
                ('description_large', ckeditor.fields.RichTextField()),
                ('description_extra', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('orden', models.IntegerField()),
                ('en_menu', models.BooleanField(default=True)),
                ('en_breadcrumbs', models.BooleanField(default=True)),
                ('meta_title', models.CharField(max_length=50)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=250)),
                ('meta_author', models.CharField(max_length=45)),
                ('xmlsitemap', models.BooleanField(default=True)),
                ('xmlsitemap_prioridad', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('title_hidden', models.BooleanField(default=True)),
                ('description_short', ckeditor.fields.RichTextField()),
                ('description_large', ckeditor.fields.RichTextField()),
                ('description_extra', models.TextField()),
                ('multimedia_imagen_destacado', models.ImageField(upload_to=b'posts')),
                ('status', models.BooleanField(default=True)),
                ('orden', models.IntegerField()),
                ('meta_title', models.CharField(max_length=50)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=250)),
                ('meta_author', models.CharField(max_length=45)),
                ('xmlsitemap', models.BooleanField(default=True)),
                ('xmlsitemap_prioridad', models.CharField(max_length=4)),
                ('status_comment', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='posts.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('orden', models.IntegerField()),
                ('meta_title', models.CharField(max_length=50)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=250)),
                ('meta_author', models.CharField(max_length=45)),
                ('xmlsitemap', models.BooleanField(default=True)),
                ('xmlsitemap_prioridad', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='posts.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
