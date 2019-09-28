from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from restaff.core.base.models import Position, Skill
from restaff.api.hr.models import Vacancy


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        _('first_name'), max_length=128)
    last_name = models.CharField(
        _('last_name'), max_length=128)
    surname = models.CharField(
        _('surname'), max_length=128)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='employees')
    experience = models.PositiveIntegerField(
        _('experience'), default=0)
    skills = models.ManyToManyField(Skill)


class Propose(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.PROTECT)

class Subscribe(models.Model):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='subscribes')
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name='subscribes')