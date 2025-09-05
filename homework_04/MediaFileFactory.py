from AudioFile import AudioFile
from MediaFile import MediaFile
from MediaType import MediaType
from PhotoFile import PhotoFile
from VideoFile import VideoFile
from LocalStorageHandler import LocalStorageHandler
from RemoteServerHandler import RemoteStorageHandler
from S3StorageHandler import S3StorageHandler
from StorageHandler import StorageHandler
from StorageType import StorageType


class MediaFileFactory:
    """Фабрика для создания объектов медиа-файлов"""

    @staticmethod
    def create_media_file(media_type: MediaType, file_path, storage_type: StorageType) -> MediaFile:

        # Создаем обработчик хранилища
        storage_handler = MediaFileFactory._create_storage_handler(storage_type)

        # Создаем соответствующий тип медиа-файла
        if media_type == MediaType.AUDIO:
            return AudioFile(
                file_path, storage_type, storage_handler
            )
        elif media_type == MediaType.VIDEO:
            return VideoFile(
                file_path, storage_type, storage_handler
            )
        elif media_type == MediaType.PHOTO:
            return PhotoFile(
                file_path, storage_type, storage_handler
            )
        else:
            raise ValueError(f"Unsupported media type: {media_type}")

    @staticmethod
    def _create_storage_handler(storage_type: StorageType) -> StorageHandler:
        if storage_type == StorageType.LOCAL:
            return LocalStorageHandler()
        elif storage_type == StorageType.S3:
            return S3StorageHandler()
        elif storage_type == StorageType.REMOTE_SERVER:
            return RemoteStorageHandler()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")