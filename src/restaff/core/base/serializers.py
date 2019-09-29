from rest_framework import serializers

from restaff.core.base.models import Position, Skill
from restaff.api.expert.models import StaffOrder, Requirement, TodoList, TodoListItem


class TodoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoListItemSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ('items', 'id')


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'

class StaffOrderCreateSerializer(serializers.ModelSerializer):
    requirements = RequirementSerializer(many=True)

    class Meta:
        model = StaffOrder
        fields = ('requirements', 'position', 'amount', 'description')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Position
        fields = '__all__'

    def get_skills(self, position):
        return SkillSerializer(
            instance=position.skills.all(),
            many=True
        ).data
