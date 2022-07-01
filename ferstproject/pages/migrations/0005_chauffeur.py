# Generated by Django 3.2.3 on 2021-05-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_client_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='chauffeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='profilCheuffaur')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('tele', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]