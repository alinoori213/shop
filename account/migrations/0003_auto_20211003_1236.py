# Generated by Django 3.2.7 on 2021-10-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='country',
        ),
        migrations.AddField(
            model_name='discount',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
