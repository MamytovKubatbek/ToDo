# Generated by Django 4.2 on 2023-04-26 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
