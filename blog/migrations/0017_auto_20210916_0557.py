# Generated by Django 3.1.5 on 2021-09-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210916_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='متن'),
        ),
    ]
