# Generated by Django 3.2.4 on 2021-06-08 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20210608_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxi',
            name='mtrc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.chauffeur'),
        ),
    ]
