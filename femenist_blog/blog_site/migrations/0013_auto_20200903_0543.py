# Generated by Django 3.1 on 2020-09-03 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0012_auto_20200903_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post_comments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_site.blog_post_comments'),
        ),
    ]
