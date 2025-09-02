from abc import ABC, abstractmethod
import datetime
import getpass

class MediaFile(ABC):
    def __init__(self, path):
        self.__path = path
        self.__creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__owner = getpass.getuser()
        print(f'Media file has been created: {self}')

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path
        print('Path set to', path)

    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date
        print('Creation date set to', creation_date)

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner
        print('Owner set to', owner)

    def __str__(self):
        return f'path:{self.__path}, creation_date:{self.__creation_date}, owner:{self.__owner}'

    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def change(self, path):
        pass