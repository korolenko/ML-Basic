from abc import ABC, abstractmethod

class StorageHandler(ABC):
    """Абстрактный класс для работы с различными хранилищами"""

    @abstractmethod
    def upload_file(self, local_path: str, remote_path: str):
        pass

    @abstractmethod
    def download_file(self, remote_path: str, local_path: str):
        pass

    @abstractmethod
    def delete_file(self, path: str):
        pass
