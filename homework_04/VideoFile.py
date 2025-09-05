from MediaFile import MediaFile
from StorageHandler import StorageHandler
from StorageType import StorageType

class VideoFile(MediaFile):
    def __init__(self, path, storage_type: StorageType, storage_handler: StorageHandler):
        super().__init__(path,storage_type,storage_handler)
        self.video_format = '16:9'
        self.fps = 24

    def change_fps(self, fps: int = 1):
        print(f"Changed fps to {fps}")
        self.fps = fps

    def change_video_format(self, video_format: str):
        print(f"Changed video format to {video_format}")
        self.video_format = video_format

