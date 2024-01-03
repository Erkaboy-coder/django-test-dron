from typing import List as list

class DronUseCase:
    def get_all(self):
        pass

    def get_by_id(self, id: int):
        pass

    def get_by_ids(self, ids: list[int]):
        pass

    def get_avaibles(self):
        pass
    def get_by_category_id(self, category_id: int):
        pass

    def get_with_pagination(self, drons, search_key: str, page_number: int, page_size: int):
        pass

    def create(self, serial_number: str, category_id: int,battery_capacity:int):
        pass

    def update(self, id: int, serial_number: str, category_id: int,battery_capacity:int):
        pass

    def delete(self, id: int):
        pass

    def status_change(self, id:int, status: int):
        pass

    def filter(self, ormData=None, search_key: str = None, serial_number: str = None, category_id: int = None,
               battery_capacity: int = None):
        pass


class DronCategoryUseCase:
    def get_by_id(self, id: str):
        pass

    def get_all(self):
        pass

    def create(self, name: str, weight_limit:int):
        pass

    def update(self, id: int, name: str, weight_limit:int):
        pass

    def delete(self, id: int):
        pass

class MedicationUseCase:
    def get_by_id(self, id: str):
        pass

    def get_all(self):
        pass

    def create(self, name: str, weight:int, code:str,img):
        pass

    def update(self, id: int, name: str, weight_limit:int):
        pass

    def delete(self, id: int):
        pass

class DeliveryUseCase:

    def get_all(self):
        pass

    def get_dron_ids(self):
        pass

    def get_by_id(self, id: str):
        pass

    def create(self, dron_id:int, medication_id:int):
        pass

    def get_by_state_and_dron_id(self, dron_id: int,state:int):
        pass

    def update(self, id: int, dron_id:int, medication_id:int):
        pass
    def delete(self, id: int):
        pass

    def change_state(self, dron_id: int, medication_id: int, state: int):
        pass


