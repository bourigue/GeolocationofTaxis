# Generated by Django 3.2.4 on 2021-06-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_orderchauffeur_id_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderchauffeur',
            name='id_chofo',
            field=models.CharField(default=9, max_length=200),
            preserve_default=False,
        ),
    ]
