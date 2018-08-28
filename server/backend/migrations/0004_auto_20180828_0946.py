# Generated by Django 2.1 on 2018-08-28 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20180827_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='perpercentage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='create_time',
            field=models.PositiveIntegerField(default=1535420802),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.PositiveIntegerField(verbose_name=1535420802),
        ),
    ]