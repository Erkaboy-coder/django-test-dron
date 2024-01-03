from usecases.core import FileUseCase
class Logger:

    def log(self, function_name:str, is_pass:bool=True, input_date:str=''):
        if is_pass:
            print(f"+ {function_name} input-> {input_date}")
        else:
            print(f"- {function_name} input-> {input_date}")

class FileService(FileUseCase, Logger):

    def __init__(self, fileModel):
        self.orm = fileModel.objects

    def get_all(self):
        return self.orm.all()

    def get_by_id(self, id: int):
        data = self.orm.filter(id=id).first()
        self.log('FileService:get_by_id', input_date=id)
        return data

    def create(self, title: str, path:str):
        file = self.orm.create(title=title, path=path)
        file.save()
        self.log('FileService:create', input_date=title)
        return file

    def update(self, id: int, title: str, path:str):
        file = self.orm.filter(id=id).first()
        file.title = title
        file.path = path
        file.save()
        self.log('FileService:update', input_date=title)
        return file

    def delete(self, id: int):
        file = self.orm.filter(id=id).first()
        file.delete()
        self.log('FileService:delete', input_date=id)
        return id






