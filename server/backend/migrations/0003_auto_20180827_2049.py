# Generated by Django 2.1 on 2018-08-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180827_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminoperationrecord',
            name='object',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='create_time',
            field=models.PositiveIntegerField(default=1535374175),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.PositiveIntegerField(verbose_name=1535374175),
        ),
    ]
