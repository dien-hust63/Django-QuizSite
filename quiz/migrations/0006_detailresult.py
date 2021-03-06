# Generated by Django 3.2 on 2021-05-05 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20210427_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailResult',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField(verbose_name='Question ID')),
                ('answer_list', models.CharField(blank=True, max_length=255, null=True, verbose_name='Answer List')),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.result')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
