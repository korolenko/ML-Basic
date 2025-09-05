from StorageHandler import StorageHandler

class RemoteStorageHandler(StorageHandler):
    """Реализация работы с удаленным сервером"""

    def __init__(self):
        print('RemoteStorageHandler created')

    def upload_file(self, local_path: str, remote_path: str):
        print(f'RemoteStorageHandler: file {local_path} is uploaded to {remote_path}')

    def download_file(self, remote_path: str, local_path: str):
        print(f'RemoteStorageHandler: file {remote_path} is downloaded to {local_path}')

    def delete_file(self, path: str):
        print(f'RemoteStorageHandler: file {path} is deleted')