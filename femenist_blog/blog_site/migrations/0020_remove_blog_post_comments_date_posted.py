# Generated by Django 3.1 on 2020-09-04 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0019_blog_post_comments_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post_comments',
            name='date_posted',
        ),
    ]