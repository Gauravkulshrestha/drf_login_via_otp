# Generated by Django 4.0.3 on 2022-03-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, verbose_name='Phone_number'),
        ),
    ]