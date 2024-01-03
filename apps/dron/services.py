from usecases.dron import DronUseCase, DeliveryUseCase, DronCategoryUseCase, MedicationUseCase
from apps.core.services import Logger
from django.db.models import Q
from typing import List as list

class DronCategoryService(DronCategoryUseCase, Logger):

    def __init__(self, bookCategoryModel):
        self.orm = bookCategoryModel.objects

    def get_all(self):
        return self.orm.all()

    def get_by_id(self, id: int):
        data = self.orm.filter(id=id).first()
        self.log('DronCategory:get_by_id', input_date=id)
        return data

    def create(self, name:str, weight_limit:int):
        category = self.orm.create(name=name,weight_limit=weight_limit)
        category.save()
        self.log('DronCategory:create', input_date=name)
        return category

    def update(self, id: int, name: str,weight_limit:int):
        category = self.orm.filter(id=id).first()
        category.name = name
        category.weight_limit = weight_limit
        category.save()
        self.log('DronCategory:update', input_date=name)
        return category

    def delete(self, id: int):
        category = self.orm.filter(id=id).first()
        category.delete()
        self.log('DronCategory:delete', input_date=id)
        return id


class MedicationService(MedicationUseCase, Logger):

    def __init__(self, bookCategoryModel):
        self.orm = bookCategoryModel.objects

    def get_all(self):
        return self.orm.all()

    def get_by_id(self, id: int):
        data = self.orm.filter(id=id).first()
        self.log('Medication:get_by_id', input_date=id)
        return data

    def create(self, name:str, weight:float, code:str, img:str):
        category = self.orm.create(name=name,weight=weight,code=code,img=img)
        category.save()
        self.log('Medication:create', input_date=name)
        return category

    def update(self, id: int, name: str,weight_limit:int):
        category = self.orm.filter(id=id).first()
        category.name = name
        category.weight_limit = weight_limit
        category.save()
        self.log('Medication:update', input_date=name)
        return category

    def delete(self, id: int):
        category = self.orm.filter(id=id).first()
        category.delete()
        self.log('Medication:delete', input_date=id)
        return id

class DronService(DronUseCase, Logger):

    def __init__(self, bookModel):
        self.orm = bookModel.objects

    def get_all(self):
        return self.orm.all()

    def get_by_id(self, id: int):
        data = self.orm.filter(id=id).first()
        self.log('BookService:get_by_id', input_date=id)
        return data

    def get_by_ids(self, ids: list[int]):
        return self.orm.filter(id__in=ids)

    def get_by_category_id(self, category_id: int):
        return self.orm.filter(category_id=category_id)

    def filter(self, ormData=None, search_key=None, author=None, language=None, year=None, allExec=True):
        books = ormData
        # if ormData:
        #     books = ormData
        if allExec is True:
            return books.filter(Q(title__icontains=search_key), Q(author__icontains=author), Q(language=language) | Q(year=year))

        query = Q()
        if search_key is not None:
            query |= Q(title__icontains=search_key)

        if author is not None:
            query |= Q(author__icontains=author)

        if type(language) == int:
            query |= Q(language=language)

        if type(year) == int:
            query |= Q(year=year)


        return books.filter(query)

    def create(self, serial_number: str,battery_capacity:int, category_id:int):
        dron = self.orm.create(
            serial_number=serial_number,battery_capacity=battery_capacity,category_id=category_id)
        dron.save()
        return dron

    def update(self, id: int, serial_number: str,battery_capacity:int, category_id:int):
        data = self.orm.filter(id=id).first()
        data.serial_number=serial_number
        data.battery_capacity=battery_capacity
        data.category_id=category_id
        data.save()
        return data

    def delete(self, id: int):
        book = self.orm.filter(id=id).first()
        book.delete()
        self.log('DronService:delete', input_date=id)
        return id


class DeliveryService(DeliveryUseCase, Logger):

    def __init__(self, deliveryModel):
        self.orm = deliveryModel.objects

    def get_all(self):
        return self.orm.all()

    def get_by_id(self, id: int):
        data = self.orm.filter(id=id).first()
        self.log('DelivaryService:get_by_id', input_date=id)
        return data

    def get_by_state_and_dron_id(self, dron_id: int,state:int):
        data = self.orm.filter(dron_id=dron_id, state=state).first()
        self.log('DelivaryService:get_by_state_and_dron_id', input_date=dron_id)
        return data

    def get_by_category(self, category_id: int):
        return

    def create(self, dron_id:int, medication_id:int):
        enroll = self.orm.create(dron_id=dron_id, medication_id=medication_id)
        enroll.save()
        return enroll

    def update(self, id: int, dron_id:int, medication_id:int):
        enroll = self.orm.filter(id=id).first()
        enroll.dron_id=dron_id
        enroll.medication_id=medication_id
        enroll.save()
        return enroll

    def change_state(self,dron_id: int, medication_id: int,state:int):
        enroll = self.orm.filter(dron_id=dron_id,medication_id=medication_id).first()
        enroll.state = state
        enroll.save()
        return enroll

