# Generated by Django 4.0.6 on 2022-07-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
