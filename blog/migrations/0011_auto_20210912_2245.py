# Generated by Django 3.1.5 on 2021-09-13 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blog_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]