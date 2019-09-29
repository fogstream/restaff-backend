from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound

from rest_framework.response import Response
from rest_framework.views import APIView

from restaff.api.employee.models import Subscribe
from restaff.api.employee.serializers import ProfileSerializer, SkillSerializer, OffersSerializer
from restaff.core.base.models import Skill, Position
from restaff.api.hr.models import Vacancy, Propose
from restaff.core.base.serializers import PositionSerializer


class ProfileView(APIView):
    @swagger_auto_schema(responses={200: ProfileSerializer()})
    def get(self, request, *args, **kwargs):
        return JsonResponse(ProfileSerializer(
            instance=request.employee
        ).data)


class SkillsView(APIView):
    @swagger_auto_schema(responses={200: SkillSerializer(many=True)})
    def get(self, request):
        return JsonResponse(SkillSerializer(
            instance=Skill.objects.all(),
            many=True
        ).data, safe=False)

class SkillView(APIView):
    @swagger_auto_schema(responses={200: SkillSerializer()})
    def get(self, request, skill_id):
        return JsonResponse(SkillSerializer(
            instance=get_object_or_404(
                request.employee.skills.all(),
                id=skill_id
            )
        ).data)

    def post(self, request, skill_id):
        skill = get_object_or_404(Skill.objects.all(), pk=skill_id)
        request.employee.skills.add(skill)
        return JsonResponse({})

    def delete(self, request, skill_id):
        skill = get_object_or_404(Skill.objects.all(), pk=skill_id)
        request.employee.skills.remove(skill)
        return Response({})


class OffersView(APIView):
    @swagger_auto_schema(responses={200: OffersSerializer(many=True)})
    def get(self, request):
        qs = Vacancy.objects.filter(
            position__in=request.employee.subscribes.values('position')
        )
        return JsonResponse(OffersSerializer(
            instance=qs, many=True
        ).data, safe=False)


class OffersOneView(APIView):
    @swagger_auto_schema(responses={200: OffersSerializer()})
    def get(self, request, offer_id):
        offer = get_object_or_404(
            Vacancy.objects.all(), id=offer_id)
        return JsonResponse(OffersSerializer(
            instance=offer
        ).data)


class OfferProposeView(APIView):
    def post(self, request, offer_id):
        vacancy = get_object_or_404(Vacancy.objects.all(), id=offer_id)
        Propose.objects.create(
            employee=request.employee,
            vacancy=vacancy
        )
        return JsonResponse({})


class PositionProposeView(APIView):
    def post(self, request, position_id):
        vacancies = Vacancy.objects.filter(
            active=True, position_id=position_id
        )
        if vacancies.exists():
            for vacancy in vacancies:
                Propose.objects.create(
                    employee=request.employee,
                    vacancy_id=vacancy
                )
        else:
            raise NotFound()

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


class SubscribePositionView(APIView):
    def post(self, request, position_id:int):
        position = get_object_or_404(
            Position.objects.all(), pk=position_id
        )
        Subscribe.objects.update_or_create(
            position=position,
            employee=request.employee
        )
        return JsonResponse({})
