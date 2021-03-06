# Generated by Django 2.2.7 on 2020-01-09 12:28

import articles.models
from django.db import migrations, models
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('articles', '0002_auto_20200106_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('writer', models.CharField(max_length=100, verbose_name='Writer')),
                ('genre', models.CharField(choices=[('adventure', 'Adventure'), ('fiction', 'Fiction'), ('non_fiction', 'Non Fiction'), ('technology', 'Technology'), ('lifestyle', 'Lifestyle')], max_length=20, verbose_name='Genre')),
                ('published_on', models.DateTimeField(auto_now_add=True, verbose_name='Published on')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Modified on')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to=articles.models.upload_image, verbose_name='Title Image')),
                ('body', tinymce.models.HTMLField(verbose_name='Content')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('keywords', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Keywords')),
            ],
        ),
        migrations.DeleteModel(
            name='articles',
        ),
    ]
