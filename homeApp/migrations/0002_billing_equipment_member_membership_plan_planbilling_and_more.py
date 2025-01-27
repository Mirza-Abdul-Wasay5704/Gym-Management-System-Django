# Generated by Django 5.1.1 on 2024-11-12 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('billing_date', models.DateField()),
                ('payment_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('join_date', models.DateField()),
                ('dob', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_months', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplierEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.equipment')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerAssignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.member')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.equipment')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.trainer')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='billing',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.membership'),
        ),
        migrations.AddField(
            model_name='membership',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.plan'),
        ),
        migrations.AddField(
            model_name='planbilling',
            name='billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.billing'),
        ),
        migrations.AddField(
            model_name='planbilling',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeApp.plan'),
        ),
        migrations.CreateModel(
            name='TrainerSpecialty',
            fields=[
                ('trainer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homeApp.trainer')),
                ('specialty', models.CharField(max_length=100)),
            ],
        ),
    ]
