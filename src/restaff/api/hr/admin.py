from django.contrib import admin

from restaff.api.hr.models import Hr, Vacancy


@admin.register(Hr)
class HrAdmin(admin.ModelAdmin):
    ...


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    ...

