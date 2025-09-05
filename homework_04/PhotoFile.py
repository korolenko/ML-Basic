from MediaFile import MediaFile
from StorageHandler import StorageHandler
from StorageType import StorageType

class PhotoFile(MediaFile):
    def __init__(self, path, storage_type: StorageType, storage_handler: StorageHandler):
        super().__init__(path, storage_type, storage_handler)
        self.__filter_name = 'default'

    def set_filter(self, filter_name: str):
        print(f"Applying {filter_name} filter to image")
        self.__filter_name = filter_name
