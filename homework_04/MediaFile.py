from abc import ABC
import datetime
import getpass

from StorageType import StorageType
from StorageHandler import StorageHandler


class MediaFile(ABC):
    """Абстрактный базовый класс для медиа-файлов"""
    def __init__(self, path, storage_type: StorageType,storage_handler: StorageHandler):
        self.__path = path
        self.__creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__owner = getpass.getuser()
        self.storage_type = storage_type
        self.storage_handler = storage_handler
        print(f'Media file has been created: {self}')

    def download(self, from_path):
        return self.storage_handler.download_file(from_path, self.__path)

    def upload(self, to_path: str):
        return self.storage_handler.upload_file(self.__path, to_path)

    def delete(self) -> bool:
        return self.storage_handler.delete_file(self.__path)

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path
        print(f'Path set to: {path}')

    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date
        print(f'Creation date set to: {creation_date}')

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner
        print(f'Owner set to: {owner}')

    def __str__(self):
        return f'path: {self.__path}, creation_date: {self.__creation_date}, owner: {self.__owner}'
