# Generated by Django 5.1.1 on 2024-11-23 20:06

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0010_alter_membership_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='additional_charges',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
