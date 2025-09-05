from MediaFile import MediaFile
from StorageHandler import StorageHandler
from StorageType import StorageType

class AudioFile(MediaFile):
    def __init__(self, path, storage_type: StorageType, storage_handler: StorageHandler):
        super().__init__(path,storage_type,storage_handler)
        self.bitrate = 100

    def convert_bitrate(self, target_bitrate):
        print(f"Converting audio to {target_bitrate} bitrate")
        self.bitrate = target_bitrate

    def __str__(self):
        return f'path: {self.path}, creation_date: {self.creation_date}, owner: {self.owner}, bitrate: {self.bitrate}'