from rest_framework import serializers

from restaff.api.employee.models import Employee
from restaff.api.expert.models import Training


class PadawanSeralizer(serializers.ModelSerializer):
    target_position = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def get_target_position(self, employee):
        trainig = Training.objects.filter(employee=employee).first()
        if trainig:
            return trainig.vacancy.position.name
        else:
            return None