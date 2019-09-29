from django.contrib import admin

from restaff.core.base.models import Skill, Position


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    ...


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    ...
