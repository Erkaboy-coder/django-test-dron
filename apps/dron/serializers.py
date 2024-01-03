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
    product = serializers.SerializerMethodField(read_only=True)
    category = DronCategorySerializer(read_only=True)
    class Meta:
        model = DronModel
        fields = [
            'id',
            'uuid',
            'serial_number',
            'battery_capacity',
            'product',
            'category',
            'updated_at',
            'created_at',
        ]
    def get_product(self, obj):
        try:
            product = DeliveryModel.objects.filter(dron_id=obj.id).last()
            obj = MedicationModel.objects.filter(id=product.medication.id).first()
            content = MedicationsSerializer(obj, many=False).data
            content['state'] = product.state
            return content
        except Exception as err:
            return []


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


