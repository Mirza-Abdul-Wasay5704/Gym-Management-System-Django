# Generated by Django 5.1.1 on 2024-11-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_memberlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='duration_months',
            field=models.IntegerField(),
        ),
    ]
