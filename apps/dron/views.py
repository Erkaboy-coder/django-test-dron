from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.core.models import FileModel
from apps.core.services import FileService
from usecases.core import FileUseCase
from helpers.constants import *
from apps.dron.models import DronModel, DronCategoryModel, MedicationModel, DeliveryModel
from apps.dron.services import DronService, DronCategoryService, DeliveryService, MedicationService
from usecases.dron import DronUseCase, DronCategoryUseCase, MedicationUseCase, DeliveryUseCase

from apps.dron.serializers import DronsSerializer, DronCategorySerializer, LoadSerializer
from helpers.helper import Helper
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

class IndexView:
    dronService: DronUseCase = DronService(DronModel)
    categoryService: DronCategoryService = DronCategoryService(DronCategoryModel)
    fileService: FileUseCase = FileService(FileModel)
    deliveryService: DeliveryUseCase = DeliveryService(DeliveryModel)
    medicationService: MedicationUseCase = MedicationService(MedicationModel)
    helper: Helper = Helper()
    dronsSerializer = DronsSerializer
    loadSerializer = LoadSerializer


# my changes test2 again
class GetDronsAPI(APIView, IndexView):
    def get(self, request):
        objs = self.dronService.get_all()
        serializers = DronsSerializer(objs, many=True)
        return Response(data=serializers.data)


class GetDronCategoriesAPI(APIView, IndexView):
    def get(self, request):
        drons = self.dronService.get_all()
        categories = self.categoryService.get_all()
        categories = DronCategorySerializer(categories, many=True).data

        for cat in categories:
            dron_ids = self.dronService.get_by_category_id(
                cat.get('id'))
            cat['count'] = len(dron_ids)

        content = {
            'categories': categories
        }
        return Response(data=content, status=status.HTTP_200_OK)


class DronCategoryActionsAPI(APIView, IndexView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        weight_limit = request.data.get('weight_limit')
        category = self.categoryService.create(name, weight_limit)
        res_data = DronCategorySerializer(category, many=False).data
        return Response(data=res_data, status=status.HTTP_201_CREATED)

    def put(self, request):
        id = request.data.get('id')
        category = self.categoryService.get_by_id(id)
        if not category:
            return Response('Category not found', status=status.HTTP_404_NOT_FOUND)

        name = request.data.get('name')
        weight_limit = request.data.get('weight_limit')
        category = self.categoryService.update(id, name,weight_limit)
        res_data = DronCategorySerializer(category, many=False).data
        return Response(data=res_data, status=status.HTTP_200_OK)

    def delete(self, request):
        id = request.data.get('id')
        category = self.categoryService.get_by_id(id)
        if not category:
            return Response('Category not found', status=status.HTTP_404_NOT_FOUND)
        content = self.categoryService.delete(id)
        return Response(data=f"{content} deleted", status=status.HTTP_204_NO_CONTENT)

class DronActionsAPI(APIView, IndexView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serial_number = request.data.get('serial_number')
        category_id = request.data.get('category_id')
        battery_capacity = request.data.get('battery_capacity')
        try:
            with transaction.atomic():
                category = self.categoryService.get_by_id(category_id)
                if not category:
                    return Response('Category not found', status=status.HTTP_404_NOT_FOUND)

                res_data = self.dronService.create(serial_number=serial_number, category_id=category_id, battery_capacity=battery_capacity)
                res_data = self.dronsSerializer(res_data, many=False).data
                return Response(data=res_data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)

    def put(self, request):
        serial_number = request.data.get('serial_number')
        category_id = request.data.get('category_id')
        battery_capacity = request.data.get('battery_capacity')
        id = request.data.get('id')
        try:
            with transaction.atomic():
                dron = self.dronService.get_by_id(id=id)
                if not dron:
                    return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)

                category = self.categoryService.get_by_id(category_id)
                if not category:
                    return Response('Category not found', status=status.HTTP_404_NOT_FOUND)

                data = self.dronService.update(id=id, serial_number=serial_number, category_id=category_id,battery_capacity=battery_capacity)
                res_data = self.dronsSerializer(data, many=False).data
                return Response(data=res_data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)

    def delete(self, request):
        id = request.data.get('id')
        book = self.dronService.get_by_id(id)
        if not book:
            return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)
        try:
            with transaction.atomic():
                data = self.dronService.delete(id)
                return Response(data=f"{data} is deleted", status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)


class DeliverProductAPI(APIView, IndexView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dron_id = request.data.get('dron_id')
        name = request.data.get('name')
        weight = request.data.get('weight')
        code = request.data.get('code')
        img = request.FILES.get('img')

        try:
            with transaction.atomic():
                dron = self.dronService.get_by_id(id=dron_id)
                if not dron:
                    return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)

                dron_avaible_check = self.deliveryService.get_by_state_and_dron_id(dron_id=dron_id, state=productStates.IDLE)
                if dron_avaible_check:
                    return Response(data={'message': "This drone is busy"}, status=400)

                if dron.battery_capacity <= 10:
                    return Response(data={'message': "Battery is not enough"}, status=400)

                if dron.category.weight_limit < int(weight):
                    return Response(data={'message':"Overloaded"}, status=400)

                medication = self.medicationService.create(name=name, weight=weight,code=code,img=img)
                res = self.deliveryService.create(medication_id=medication.id, dron_id=dron_id)
                res_data = self.loadSerializer(res, many=False).data
                return Response(data=res_data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)

    def put(self, request):
        serial_number = request.data.get('serial_number')
        category_id = request.data.get('category_id')
        battery_capacity = request.data.get('battery_capacity')
        id = request.data.get('id')
        try:
            with transaction.atomic():
                dron = self.dronService.get_by_id(id=id)
                if not dron:
                    return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)

                category = self.categoryService.get_by_id(category_id)
                if not category:
                    return Response('Category not found', status=status.HTTP_404_NOT_FOUND)

                data = self.dronService.update(id=id, serial_number=serial_number, category_id=category_id,battery_capacity=battery_capacity)
                res_data = self.dronsSerializer(data, many=False).data
                return Response(data=res_data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)

    def delete(self, request):
        id = request.data.get('id')
        book = self.dronService.get_by_id(id)
        if not book:
            return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)
        try:
            with transaction.atomic():
                data = self.dronService.delete(id)
                return Response(data=f"{data} is deleted", status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)

class DeliverProductStatusChangerAPI(APIView, IndexView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dron_id = request.data.get('dron_id')
        medication_id = request.data.get('medication_id')
        state = request.data.get('state')

        try:
            with transaction.atomic():
                dron = self.dronService.get_by_id(id=dron_id)
                if not dron:
                    return Response('Dron not found', status=status.HTTP_404_NOT_FOUND)

                medication = self.medicationService.get_by_id(id=medication_id)
                if not medication:
                    return Response('Medication not found', status=status.HTTP_404_NOT_FOUND)

                deliver = self.deliveryService.change_state(dron_id=dron_id,medication_id=medication_id,state=state)
                res_data = self.loadSerializer(deliver, many=False).data
                return Response(data=res_data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={'message':format(str(err))}, status=400)
