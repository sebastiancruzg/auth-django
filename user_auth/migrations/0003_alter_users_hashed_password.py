# Generated by Django 5.1.3 on 2024-11-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_users_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='hashed_password',
            field=models.CharField(max_length=74),
        ),
    ]
