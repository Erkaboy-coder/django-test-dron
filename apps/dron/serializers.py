from rest_framework import serializers
from apps.core.serializers import FileSerializer
from .models import DronModel,DronCategoryModel, DeliveryModel, MedicationModel

class DronCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DronCategoryModel
        fields = [
            'id',
            'uuid',
            'name',
            'weight_limit',
            'updated_at',
            'created_at',
        ]

class DronsSerializer(serializers.ModelSerializer):

    category = DronCategorySerializer(read_only=True)
    class Meta:
        model = DronModel
        fields = [
            'id',
            'uuid',
            'serial_number',
            'battery_capacity',
            'category',
            'updated_at',
            'created_at',
        ]

class MedicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationModel
        fields = [
            'id',
            'uuid',
            'name',
            'weight',
            'code',
            'img',
            'updated_at',
            'created_at',
        ]

class LoadSerializer(serializers.ModelSerializer):

    dron = DronsSerializer(read_only=True)
    medication = MedicationsSerializer(read_only=True)
    class Meta:
        model = DeliveryModel
        fields = [
            'id',
            'uuid',
            'dron',
            'state',
            'medication',
            'updated_at',
            'created_at',
        ]


