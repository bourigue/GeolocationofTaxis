# Generated by Django 3.2.3 on 2021-05-31 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_taxi'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=133)),
                ('my_file', models.FileField(upload_to='profilClient')),
            ],
        ),
    ]
