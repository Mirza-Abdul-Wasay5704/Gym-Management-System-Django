# Generated by Django 5.1.1 on 2024-11-20 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0006_alter_plan_duration_months'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrainerSpecialty',
            new_name='TrainerSpeciality',
        ),
        migrations.RenameField(
            model_name='trainerspeciality',
            old_name='specialty',
            new_name='speciality',
        ),
    ]
