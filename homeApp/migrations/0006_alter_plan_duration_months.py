# Generated by Django 5.1.1 on 2024-11-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0005_alter_plan_duration_months'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='duration_months',
            field=models.PositiveIntegerField(),
        ),
    ]
