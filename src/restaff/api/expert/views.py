from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from restaff.api.employee.models import Employee
from restaff.api.expert.serializers import Padawan
from restaff.api.expert.models import StaffOrder, Trainig, TodoList
from restaff.core.base.serializers import TodoListSerializer, StaffOrderCreateSerializer


def padawans_queryset():
    return Trainig.objects.filter().annotate(
        first_name='employee__first_name',
        last_name='employee__last_name',
        surname='employee__surname',
        position='vacancy__position__name',
        target_position='employee__position__name'
    )

class Padawans(APIView):
    def get(self, request):
        padawans = padawans_queryset().filter(
            expert=request.expert
        )
        return JsonResponse(data=[
            Padawan(data=padawan).data for padawan in padawans
        ])


class PadawansOne(APIView):
    def get(self, request, padawan_id:int):
        employee = get_object_or_404(
            Employee.objects.all().select_related(
                'position'
            ), pk=padawan_id
        )
        return JsonResponse(data=Padawan(dict(
            first_name=employee.first_name,
            last_name=employee.last_name,
            surname=employee.surname,
            current_position=employee.position.name
        )).data)


class PadawanTodoListOne(APIView):
    def get(self, request, padawan_id:int):
        todo_list = TodoList.objects.get(
            training__expert=request.expert,
            training__employee__id=padawan_id
        )
        return JsonResponse(TodoListSerializer(
            instance=todo_list
        ).data)

    def post(self, request, padawan_id:int):
        todo_list_serializer = TodoListSerializer(data=request.data)
        todo_list_serializer.is_valid(raise_exception=True)

        return JsonResponse(todo_list_serializer.validated_data)


class StaffOrdersView(APIView):
    def get(self, request):
        return JsonResponse(data=StaffOrderCreateSerializer(
            instance=StaffOrder.objects.all(),
            many=True
        ).data)


class StaffOrdersOneView(APIView):
    def get(self, request, staff_order_id):
        staff_order = get_object_or_404(
            StaffOrder.objects.all(),
            pk=staff_order_id
        )
        return JsonResponse(data=StaffOrderCreateSerializer(
            instance=staff_order
        ).data)


    def post(self, request):
        serializer = StaffOrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return JsonResponse(data=serializer.data)
