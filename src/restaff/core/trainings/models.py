from django.db import models
from django.utils.translation import gettext as _

from restaff.api.employee.models import Employee
from restaff.api.expert.models import Expert
from restaff.core.base.models import Position, Skill
from restaff.api.hr.models import Vacancy


class Trainig(models.Model):
    expert = models.ForeignKey(
        Expert, on_delete=models.PROTECT, related_name='trainings')
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name='trainings')
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.PROTECT)


class TodoList(models.Model):
    training = models.OneToOneField(
        Trainig, on_delete=models.CASCADE, related_name='todo_list')


class TodoListItem(models.Model):
    todo_list = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='items')
    skill = models.ForeignKey(
        Skill, on_delete=models.PROTECT)
    name = models.CharField(
        _('name'), max_length=128)
    checked =  models.BooleanField(
        _('checked'), default=False)
    ordering = models.PositiveIntegerField(
        _('ordering'))
    expert = models.ForeignKey(
        Expert, on_delete=models.SET_NULL, null=True, blank=True)
