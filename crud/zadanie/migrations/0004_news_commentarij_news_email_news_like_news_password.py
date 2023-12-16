# Generated by Django 5.0 on 2023-12-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadanie', '0003_news_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='commentarij',
            field=models.CharField(default=None, max_length=50, verbose_name='добавить комментарий?'),
        ),
        migrations.AddField(
            model_name='news',
            name='email',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.CharField(default='0', max_length=3, verbose_name='добавить лайки?'),
        ),
        migrations.AddField(
            model_name='news',
            name='password',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
