from django.contrib import admin

from restaff.api.employee.models import Employee, Subscribe
from restaff.api.hr.models import Propose


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...

@admin.register(Propose)
class ProposeAdmin(admin.ModelAdmin):
    ...

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    ...