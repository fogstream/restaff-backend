from django.db import models
from django.utils.translation import gettext as _


class Skill(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(_('name'), max_length=128)
    skills = models.ManyToManyField(Skill)
    salary = models.DecimalField(
        _('salary'), null=True, decimal_places=2, max_digits=16)

    def __str__(self):
        return self.name
