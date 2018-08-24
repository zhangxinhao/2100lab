# Generated by Django 2.1 on 2018-08-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180823_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='audio_url',
            field=models.FileField(blank=True, null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='course',
            name='create_time',
            field=models.PositiveIntegerField(default=1535022247),
        ),
        migrations.AlterField(
            model_name='course',
            name='profile_url',
            field=models.ImageField(blank=True, null=True, upload_to='course_picture'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='postion',
            field=models.ImageField(blank=True, null=True, upload_to='course_picture'),
        ),
    ]