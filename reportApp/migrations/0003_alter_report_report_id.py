# Generated by Django 4.1.3 on 2022-12-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportApp', '0002_alter_report_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_id',
            field=models.CharField(max_length=255),
        ),
    ]