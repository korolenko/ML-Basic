from abc import ABC
from homework_04.MediaFile import MediaFile

class AudioFile(MediaFile, ABC):
    def __init__(self, path, codec):
        super().__init__(path)
        self.codec = codec

    def read(self, path):
        print(f'Reading {path} and playing music!')

    def change(self, path):
        print(f'Changing music file located {path}...')