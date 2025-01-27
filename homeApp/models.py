from decimal import Decimal

from django.db import models
from django.contrib.auth.hashers import make_password

# 1. Members
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    join_date = models.DateField()
    dob = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# 1.1
# Member Login (admin khud id pass dega)
class MemberLogin(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)  # Link to Member table
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Login for {self.member.first_name} {self.member.last_name}"


# 2. Plans
class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField()
    def __str__(self):
        return self.plan_name

# 3. Memberships
class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Membership {self.membership_id}"


# 4. Trainers
class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=15)
    speciality = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# 5. Trainer Specialty
class TrainerSpeciality(models.Model):
    trainer = models.OneToOneField(Trainer, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.trainer}: {self.specialty}"


# 6. Trainer Assignments
class TrainerAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Assignment {self.assignment_id}"

# 7. Billing # edit add additional_charges
class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # Added field
    billing_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Billing {self.billing_id}"

# 8. Equipment
class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    purchase_date = models.DateField()
    maintenance_date = models.DateField()

    def __str__(self):
        return self.name

# 9. Suppliers
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.supplier_name

# 10. Supplier Equipment
class SupplierEquipment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.supplier}: {self.equipment_name}"

# 11. Plan Billing
class PlanBilling(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plan_name}"

# 12. Trainer Equipment
class TrainerEquipment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.trainer}: {self.equipment_name}"
