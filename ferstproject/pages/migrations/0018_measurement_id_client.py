# Generated by Django 3.2.4 on 2021-06-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20210609_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='id_client',
            field=models.CharField(default=42, max_length=200),
            preserve_default=False,
        ),
    ]