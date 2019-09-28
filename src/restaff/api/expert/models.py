from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from restaff.core.base.models import Position, Skill


class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=128)


class StaffOrder(models.Model):
    expert = models.ForeignKey(
        Expert, on_delete=models.CASCADE,  related_name='staff_orders')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE,  related_name='staff_orders')
    amount = models.PositiveIntegerField(_('amount'), default=1)
    description = models.TextField(_('description'), null=True, blank=True)
    archive = models.BooleanField(_('archived'), default=False)


class Requirement(models.Model):
    staff_order = models.ForeignKey(StaffOrder, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(_('name'), max_length=128)