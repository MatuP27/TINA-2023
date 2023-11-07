# Generated by Django 4.0.4 on 2022-06-09 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_path', models.CharField(help_text='File path in FS', max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.score')),
            ],
        ),
    ]