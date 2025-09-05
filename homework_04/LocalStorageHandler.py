from StorageHandler import StorageHandler

class LocalStorageHandler(StorageHandler):
    """Реализация работы с локальным хранилищем"""
    def __init__(self):
        print('LocalStorageHandler created')

    def upload_file(self, local_path: str, remote_path: str):
        print(f'LocalStorageHandler: file {local_path} is uploaded to {remote_path}')

    def download_file(self, remote_path: str, local_path: str):
        print(f'LocalStorageHandler: file {remote_path} is downloaded to {local_path}')

    def delete_file(self, path: str):
        print(f'LocalStorageHandler: file {path} is deleted')




