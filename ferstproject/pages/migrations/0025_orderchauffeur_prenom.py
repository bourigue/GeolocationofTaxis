# Generated by Django 3.2.4 on 2021-06-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_commande_nbrplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderchauffeur',
            name='prenom',
            field=models.CharField(default=23, max_length=200),
            preserve_default=False,
        ),
    ]
