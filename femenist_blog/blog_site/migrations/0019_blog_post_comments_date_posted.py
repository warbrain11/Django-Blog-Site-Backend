# Generated by Django 3.1 on 2020-09-04 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0018_auto_20200903_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post_comments',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
