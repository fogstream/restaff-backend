from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from restaff.api.employee.models import Employee

from restaff.core.base.models import Position, Skill


class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return self.name


class StaffOrder(models.Model):
    expert = models.ForeignKey(
        Expert, on_delete=models.CASCADE,  related_name='staff_orders', null=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE,  related_name='staff_orders')
    amount = models.PositiveIntegerField(_('amount'), default=1)
    description = models.TextField(_('description'), null=True, blank=True)
    archive = models.BooleanField(_('archived'), default=False)

    def __str__(self):
        return f'{self.position.name} / {self.amount}'


class Requirement(models.Model):
    staff_order = models.ForeignKey(StaffOrder, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(_('name'), max_length=128)

    def __str__(self):
        return self.name


class Trainig(models.Model):
    expert = models.ForeignKey(
        Expert, on_delete=models.PROTECT, related_name='trainings')
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name='trainings')
    vacancy = models.ForeignKey(
        'hr.Vacancy', on_delete=models.PROTECT)


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

    def __str__(self):
        return self.name

