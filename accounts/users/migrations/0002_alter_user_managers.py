# Generated by Django 4.0.3 on 2022-03-03 12:17

from django.db import migrations
import users.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.manager.UserManager()),
            ],
        ),
    ]
