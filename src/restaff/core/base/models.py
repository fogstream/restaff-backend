from django.db import models
from django.utils.translation import gettext as _

from restaff.api.expert.models import StaffOrder


class Skill(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)


class Position(models.Model):
    name = models.CharField(_('name'), max_length=128)
    skills = models.ManyToManyField(Skill)
    salary = models.DecimalField(_('salary'), null=True)
