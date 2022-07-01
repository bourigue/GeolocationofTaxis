# Generated by Django 3.2.4 on 2021-06-09 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_orderchauffeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderchauffeur',
            name='lat',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderchauffeur',
            name='log',
            field=models.CharField(default=1234567, max_length=200),
            preserve_default=False,
        ),
    ]
