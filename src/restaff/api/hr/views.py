from itertools import repeat

from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from restaff.api.employee.models import Employee
from restaff.api.expert.models import Expert, StaffOrder, TodoList, Training
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
        ).data, safe=False)


class StaffOrdersOne(APIView):
    @swagger_auto_schema(responses={200: StaffOrdersSerializer(many=True)})
    def get(self, request, staff_order_id:int):
        obj = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        return JsonResponse(StaffOrdersSerializer(
            instance=obj
        ).data)


class StaffOrderMakeDemand(APIView):
    def get(self, request, staff_order_id:int):
        obj: StaffOrder = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        Vacancy.objects.update_or_create(
            staff_order=obj,
            position=obj.position,
            defaults={
                'amount': obj.amount
            }
        )

        return JsonResponse({})


class StaffOrdersArchiveOne(APIView):

    def get(self, request, staff_order_id:int):
        obj: StaffOrder = get_object_or_404(
            StaffOrder.objects.all(), pk=staff_order_id)
        obj.archive = True
        obj.save()
        return JsonResponse({})


class WidgetStaffOrders(APIView):
    @swagger_auto_schema(responses={200: StaffOrdersSerializer(many=True)})
    def get(self, request):
        qs = StaffOrder.objects.all()
        return JsonResponse(StaffOrdersSerializer(
            instance=qs, many=True
        ).data, safe=False)


class WidgetVacancyView(APIView):
    @swagger_auto_schema(responses={200: WidgetVacancySerializer(many=True)})
    def get(self, request):
        qs = Position.objects.filter(
        ).annotate(
            exists_count=Count('employees'),
            vacancy_count=Count('vacancies')
        ).filter(vacancy_count__gt=0)
        return JsonResponse(WidgetVacancySerializer(
            instance=qs, many=True
        ).data, safe=False)

class EmployeesView(APIView):

    @swagger_auto_schema(responses={200: EmployeesSerializer(many=True)})
    def get(self, request):
        return JsonResponse(EmployeesSerializer(
            instance=Employee.objects.all(),
            many=True
        ).data, safe=False)


class EmployeesProfileView(APIView):
    @swagger_auto_schema(responses={200: EmployeesSerializer()})
    def get(self, request, employee_id):
        return JsonResponse(EmployeesSerializer(
            instance=get_object_or_404(
                Employee.objects.all(),
                pk=employee_id
            ),
        ).data)


class EmployeesTodoListView(APIView):
    @swagger_auto_schema(responses={200: TodoListSerializer()})
    def get(self, request, employee_id):
        todo_list = TodoList.objects.filter(
            training__employee__id=employee_id
        ).first()
        return JsonResponse(TodoListSerializer(
            instance=todo_list
        ).data)


class PositionsView(APIView):
    @swagger_auto_schema(responses={200: PositionSerializer(many=True)})
    def get(self, request):
        return JsonResponse(PositionSerializer(
            instance=Position.objects.all(),
            many=True
        ).data, safe=False)


class PositionsOneView(APIView):
    @swagger_auto_schema(responses={200: PositionSerializer()})
    def get(self, request, position_id:int):
        return JsonResponse(PositionSerializer(
            instance=get_object_or_404(
                Position.objects.all(), pk=position_id
            )
        ).data)


class PositionStaffOrdersView(APIView):
    @swagger_auto_schema(responses={200: PositionStaffOrderSerializer(many=True)})
    def get(self, request, position_id:int):
        return JsonResponse(data=PositionStaffOrderSerializer(
            instance=StaffOrder.objects.filter(
                position_id=position_id,
                archive=False
            ), many=True
        ).data, safe=False)


class PositionProposesView(APIView):
    @swagger_auto_schema(responses={200: PositionProposesSerializer(many=True)})
    def get(self, request, position_id:int):
        qs = Propose.objects.filter(
            vacancy__active=True,
            vacancy__position__id=position_id
        )
        return JsonResponse(PositionProposesSerializer(
            instance=qs, many=True
        ).data, safe=False)


class PositionPadawanProgress(APIView):
    @swagger_auto_schema(responses={200: PadawanProgressSerializer(many=True)})
    def get(self, request, position_id:int):
        return JsonResponse(PadawanProgressSerializer(
            instance=Employee.objects.filter(
                trainings__vacancy__position_id=position_id,
            ), many=True
        ).data, safe=False)


class ExpertsView(APIView):
    @swagger_auto_schema(responses={200: ExpertSerializer(many=True)})
    def get(self, request):
        return JsonResponse(ExpertSerializer(
            instance=Expert.objects.all(),
            many=True
        ).data, safe=False)


class ExpertsOneView(APIView):
    @swagger_auto_schema(responses={200: ExpertSerializer()})
    def get(self, request, expert_id:int):
        expert = get_object_or_404(Expert.objects.all(), pk=expert_id)
        return JsonResponse(ExpertSerializer(
            instance=expert
        ).data)


class ExpertsOnePadawanProgressView(APIView):
    @swagger_auto_schema(responses={200: PadawanProgressSerializer(many=True)})
    def get(self, request, expert_id:int):
        return JsonResponse(PadawanProgressSerializer(
            instance=Employee.objects.filter(
                trainings__expert_id=expert_id
            ), many=True
        ).data, safe=False)

class ProposeAcceptView(APIView):
    def post(self, request, propose_id:int):
        propose = get_object_or_404(
            Propose.objects.filter(), pk=propose_id)
        Training.objects.create(
            expert=propose.vacancy.staff_order.expert,
            employee_id=propose.employee,
            vacancy=propose.vacancy,
        )
        return JsonResponse({})
