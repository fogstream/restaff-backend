from django.contrib import admin

from restaff.api.expert.models import Expert, StaffOrder, Requirement


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    ...


class RequirementInline(admin.StackedInline):
    model = Requirement

@admin.register(StaffOrder)
class StaffOrderAdmin(admin.ModelAdmin):
    inlines = (RequirementInline,)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    ...
