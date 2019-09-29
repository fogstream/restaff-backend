from itertools import repeat

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from restaff.api.employee.models import Employee
from restaff.api.expert.models import Expert, StaffOrder, TodoList
from restaff.api.hr.serializers import StaffOrdersSerializer, WidgetVacancySerializer, EmployeesSerializer, \
    PositionStaffOrderSerializer, PositionProposesSerializer, PadawanProgressSerializer, ExpertSerializer
from restaff.core.base.models import Position
from restaff.api.hr.models import Vacancy, Propose
from restaff.core.base.serializers import TodoListSerializer, PositionSerializer


class StaffOrdersView(APIView):
    @swagger_auto_schema(responses={200: StaffOrdersSerializer(many=True)})
    def get(self, request):
        qs = StaffOrder.objects.all()
        return JsonResponse(StaffOrdersSerializer(
            instance=qs, many=True
        ).data)


class StaffOrdersOne(APIView):
    def get(self, request, staff_order_id:int):
        obj = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        return JsonResponse(StaffOrdersSerializer(
            instance=obj
        ))


class StaffOrderMakeDemand(APIView):
    def get(self, request, staff_order_id:int):
        obj: StaffOrder = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        for _ in repeat(obj, obj.amount):
            Vacancy.objects.create(
                staff_order=obj, position=obj.position)
        return JsonResponse({})


class StaffOrdersArchiveOne(APIView):
    def get(self, request, staff_order_id:int):
        obj: StaffOrder = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        obj.archive = True
        obj.save()
        return JsonResponse({})


class WidgetStaffOrders(APIView):
    def get(self, request):
        qs = StaffOrder.objects.all()
        return JsonResponse(StaffOrdersSerializer(
            instance=qs, many=True
        ).data)



class WidgetVacancyView(APIView):
    def get(self):
        qs = Position.objects.filter(
        ).annotate(
            exists_count=Count('employees'),
            vacancy_count=Count('vacancies')
        ).filter(vacancy_count__gte=0)
        return JsonResponse(WidgetVacancySerializer(
            instance=qs, many=True
        ).data)

class EmployeesView(APIView):
    def get(self):
        return JsonResponse(EmployeesSerializer(
            instance=Employee.objects.all(),
            many=True
        ).data)


class EmployeesProfileView(APIView):
    def get(self, employee_id):
        return JsonResponse(EmployeesSerializer(
            instance=get_object_or_404(
                Employee.objects.all(),
                pk=employee_id
            ),
        ).data)


class EmployeesTodoListView(APIView):
    def get(self, request):
        todo_list = TodoList.objects.filter(
            training__employee=request.exmployee
        ).first()
        return JsonResponse(TodoListSerializer(
            instance=todo_list
        ).data)


class PositionsView(APIView):
    def get(self, request):
        return JsonResponse(PositionSerializer(
            instance=Position.objects.all(),
            many=True
        ).data)


class PositionsOneView(APIView):
    def get(self, request, position_id:int):
        return JsonResponse(PositionSerializer(
            instance=get_object_or_404(
                Position.objects.all(), pk=position_id
            )
        ).data)


class PositionStaffOrdersView(APIView):
    def get(self, request, position_id:int):
        return JsonResponse(data=PositionStaffOrderSerializer(
            instance=StaffOrder.objects.filter(
                position_id=position_id,
                archive=False
            ), many=True
        ).data)


class PositionProposesView(APIView):
    def get(self, request, position_id:int):
        qs = Propose.objects.filter(
            vacancy__active=True,
            vacancy__position__id=position_id
        )
        return JsonResponse(PositionProposesSerializer(
            instance=qs, many=True
        ))


class PositionPadawanProgress(APIView):
    def get(self, request, position_id:int):
        return JsonResponse(PadawanProgressSerializer(
            instance=Employee.objects.filter(
                trainings__vacancy__position_id=position_id
            )
        ))


class ExpertsView(APIView):
    def get(self, request):
        return JsonResponse(ExpertSerializer(
            instance=Expert.objects.all(),
            many=True
        ))


class ExpertsOneView(APIView):
    def get(self, request, expert_id:int):
        expert = get_object_or_404(Expert.objects.all(), pk=expert_id)
        return JsonResponse(ExpertSerializer(
            instance=expert
        ))


class ExpertsOnePadawanProgressView(APIView):
    def get(self, request, expert_id:int):
        return JsonResponse(PadawanProgressSerializer(
            Employee.objects.filter(
                trainings__expert_id=expert_id
            )
        ))
