# Generated by Django 3.2.4 on 2021-06-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_chofochoisir'),
    ]

    operations = [
        migrations.CreateModel(
            name='finalcmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileclient', models.CharField(max_length=200)),
                ('nomclient', models.CharField(max_length=200)),
                ('prenomclient', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('nbrplace', models.CharField(max_length=200)),
                ('idcmd', models.CharField(max_length=200)),
                ('idord', models.CharField(max_length=200)),
            ],
        ),
    ]