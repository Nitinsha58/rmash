# Generated by Django 4.1.2 on 2022-11-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
