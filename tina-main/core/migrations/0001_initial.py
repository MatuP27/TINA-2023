# Generated by Django 4.0.4 on 2022-06-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter product name', max_length=20)),
                ('alias', models.CharField(help_text='Enter product alias', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Enter product score')),
                ('description', models.CharField(help_text='Enter product alias', max_length=80)),
            ],
        ),
    ]