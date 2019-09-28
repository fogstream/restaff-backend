from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from restaff.api.expert.models import StaffOrder
from restaff.core.base.models import Position


class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(_('first_name'), max_length=128)
    last_name = models.CharField(_('last_name'), max_length=128)
    surname = models.CharField(_('surname'), max_length=128)


class Vacancy(models.Model):
    staff_order = models.ForeignKey(StaffOrder, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='vacancies')
    amount = models.IntegerField(_('amount'), default=1)
    description = models.TextField(_('description'), null=True, blank=True)
    dead_line = models.DateTimeField(_('dead line'), null=True)
    active = models.DateTimeField(_('active'), default=True)

    class Meta:
        unique_together = ('position', 'staff_order')