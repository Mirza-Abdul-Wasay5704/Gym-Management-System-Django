from django.contrib import admin
from .models import Member, Plan, Membership, Trainer, TrainerSpeciality, TrainerAssignment, Billing, Equipment, Supplier, SupplierEquipment, PlanBilling, TrainerEquipment,  MemberLogin

admin.site.register(Member)
admin.site.register(Plan)
admin.site.register(Membership)
admin.site.register(Trainer)
admin.site.register(TrainerSpeciality)
admin.site.register(TrainerAssignment)
admin.site.register(Billing)
admin.site.register(Equipment)
admin.site.register(Supplier)
admin.site.register(SupplierEquipment)
admin.site.register(PlanBilling)
admin.site.register(TrainerEquipment)
admin.site.register(MemberLogin)