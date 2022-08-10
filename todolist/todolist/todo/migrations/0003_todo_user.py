# Generated by Django 4.0.6 on 2022-07-15 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
        ('todo', '0002_alter_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='Todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticator.user'),
        ),
    ]
