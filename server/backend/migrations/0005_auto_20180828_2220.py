# Generated by Django 2.1 on 2018-08-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20180828_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_time',
            field=models.PositiveIntegerField(default=1535466011),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.PositiveIntegerField(default=1535466011),
        ),
    ]
