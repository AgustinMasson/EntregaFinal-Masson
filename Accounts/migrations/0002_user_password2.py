# Generated by Django 4.0.5 on 2022-07-25 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='password2', max_length=50),
        ),
    ]
