from django.db.models import Sum
from rest_framework import serializers

from restaff.api.employee.models import Employee
from restaff.api.hr.models import Vacancy
from restaff.core.base.models import Skill, Position


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 2

    def get_skills(self, employee):
        return SkillSerializer(employee.skills.all(), many=True).data


class OffersSerializer(serializers.ModelSerializer):
    expert = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = '__all__'
        depth = 2

    def get_expert(self, offer: Vacancy):
        if offer.staff_order:
            return offer.staff_order.expert.name
        else:
            return 'HR'
