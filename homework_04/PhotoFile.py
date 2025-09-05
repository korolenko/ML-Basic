from MediaFile import MediaFile
from StorageHandler import StorageHandler
from StorageType import StorageType

class PhotoFile(MediaFile):
    def __init__(self, path, storage_type: StorageType, storage_handler: StorageHandler):
        self.filter_name = 'default'
        super().__init__(path, storage_type, storage_handler)


    def set_filter(self, filter_name: str):
        print(f"Applying {filter_name} filter to image")
        self.filter_name = filter_name

    def __str__(self):
        return f'path: {self.path}, creation_date: {self.creation_date}, owner: {self.owner}, filter_name: {self.filter_name}'