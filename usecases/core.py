class FileUseCase:
    def get_by_id(self, id: str):
        pass

    def get_all(self):
        pass

    def create(self, title: str, path:str):
        pass

    def update(self, id: int, title: str, path:str):
        pass

    def delete(self, id: int):
        pass

class ICoreService:
    def get_all(self):
        pass

    def get_by_id(self, id:int):
        pass