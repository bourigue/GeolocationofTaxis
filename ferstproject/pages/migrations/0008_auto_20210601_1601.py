# Generated by Django 3.2.3 on 2021-06-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chauffeur',
            name='profile',
            field=models.FileField(upload_to='profilCheuffaur'),
        ),
        migrations.AlterField(
            model_name='client',
            name='profile',
            field=models.FileField(upload_to='profilClient'),
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='my_file',
            field=models.FileField(upload_to='profilClientt'),
        ),
    ]
