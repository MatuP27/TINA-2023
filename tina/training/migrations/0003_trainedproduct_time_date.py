# Generated by Django 4.0.5 on 2022-06-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_remove_trainedproduct_picture_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainedproduct',
            name='time_date',
            field=models.DateField(auto_now=True),
        ),
    ]