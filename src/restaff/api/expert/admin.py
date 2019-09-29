from django.contrib import admin

from restaff.api.expert.models import Expert, StaffOrder, Requirement, Training, TodoListItem, TodoList


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


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    ...


class TodoListItemInline(admin.StackedInline):
    model = TodoListItem


@admin.register(TodoList)
class TrainingAdmin(admin.ModelAdmin):
    inlines = (TodoListItemInline, )
