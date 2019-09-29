from rest_framework import serializers

from restaff.api.employee.models import Employee
from restaff.api.hr.models import Propose
from restaff.api.expert.models import Expert, StaffOrder
from restaff.core.base.models import Position, Skill


class StaffOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffOrder
        fields = ('__all__')
        depth = 1

class WidgetVacancySerializer(serializers.ModelSerializer):
    exists_count = serializers.IntegerField()
    vacancy_count = serializers.IntegerField()

    class Meta:
        model = Position
        fields = ('id', 'name', 'exists_count', 'vacancy_count')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_skills(self, employee):
        return SkillSerializer(
            instance=employee.skills.all(),
            many=True
        ).data


class PositionStaffOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffOrder
        fields = '__all__'
        depth = 2


class PositionProposesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propose
        fields = ('id', 'employee')
        depth = 2


class PadawanProgressSerializer(serializers.ModelSerializer):
    percent = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('id', 'percent', 'employee')
        depth = 2

    def get_percent(self, obj):
        return 45

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ('id', 'name')
