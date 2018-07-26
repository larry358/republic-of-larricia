# Generated by Django 2.0.7 on 2018-07-26 01:59

from django.db import migrations, models
import larricia.models
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=larricia.models.next_id, max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('user_image', models.CharField(max_length=500, verbose_name='图片路径')),
                ('name', models.CharField(max_length=50, verbose_name='标题')),
                ('summary', models.CharField(max_length=200, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.FloatField(default=time.time)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(default=larricia.models.next_id, max_length=50, primary_key=True, serialize=False)),
                ('blog_id', models.CharField(max_length=50, verbose_name='博文id')),
                ('user_id', models.CharField(max_length=50, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.FloatField(default=time.time)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=larricia.models.next_id, max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, verbose_name='电子邮箱')),
                ('passwd', models.CharField(max_length=50, verbose_name='密码')),
                ('admin', models.BooleanField()),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('image', models.CharField(max_length=500, verbose_name='图片路径')),
                ('created_at', models.FloatField(default=time.time)),
            ],
        ),
    ]