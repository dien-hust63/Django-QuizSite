# Generated by Django 3.2 on 2021-04-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210408_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.CharField(max_length=255, unique=True, verbose_name='Content'),
        ),
    ]
