# Generated by Django 3.2.3 on 2021-09-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_auto_20210524_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='article_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='article_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
