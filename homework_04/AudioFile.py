from MediaFile import MediaFile
from StorageHandler import StorageHandler
from StorageType import StorageType

class AudioFile(MediaFile):
    def __init__(self, path, storage_type: StorageType, storage_handler: StorageHandler):
        super().__init__(path,storage_type,storage_handler)
        self.__bitrate = 100

    def set_bitrate(self, bitrate: int):
        self.__bitrate = bitrate

    def get_bitrate(self):
        return self.__bitrate

    def convert_bitrate(self, target_bitrate):
        print(f"Converting audio to {target_bitrate} bitrate")
        self.__bitrate = target_bitrate
