from django.db import models
import uuid
from apps.core.models import FileModel

# Create your models here.
class DronCategoryModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=100, blank=True)
    weight_limit =  models.IntegerField(blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "DronCategoriesModel"

class DronModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    serial_number = models.CharField(verbose_name="serial number", max_length=100, blank=True)
    category = models.ForeignKey(DronCategoryModel, blank=True, null=True, on_delete=models.CASCADE,related_name='category')
    battery_capacity = models.IntegerField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.serial_number

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "DronModel"

class MedicationModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(verbose_name="name", max_length=100, blank=True)
    weight = models.FloatField(blank=True, null=True)
    code = models.CharField(verbose_name="name", max_length=100, blank=True)
    img = models.FileField("img", upload_to='data/images/', blank=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "MedicationModel"

class DeliveryModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    dron = models.ForeignKey(DronModel, blank=True, null=True, on_delete=models.CASCADE,related_name='dron')
    state_choices=(
        (1, 'IDLE'),
        (2, 'LOADING'),
        (3, 'LOADED'),
        (4, 'DELIVERING'),
        (5, 'DELIVERED'),
        (6, 'RETURNING'),
    )
    state = models.IntegerField(choices=state_choices, default=1)
    medication = models.ForeignKey(MedicationModel, blank=True, null=True, on_delete=models.CASCADE,related_name='medication')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.dron.serial_number

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "DeliveryModel"