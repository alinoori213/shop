# Generated by Django 3.2.7 on 2021-10-03 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_discount_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discountCode', to=settings.AUTH_USER_MODEL),
        ),
    ]
