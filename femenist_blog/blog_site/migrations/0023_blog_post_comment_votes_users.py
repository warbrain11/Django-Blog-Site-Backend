# Generated by Django 3.1 on 2020-09-08 01:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0022_auto_20200908_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post_comment_votes',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
