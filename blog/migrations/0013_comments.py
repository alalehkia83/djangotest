# Generated by Django 3.1.5 on 2021-09-14 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_category_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('email', models.EmailField(max_length=254, verbose_name='آدرس الکترونیکی')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ نشر')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='مقاله')),
            ],
        ),
    ]
