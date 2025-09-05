from MediaFileFactory import MediaFileFactory
from MediaType import MediaType
from StorageType import StorageType

if __name__ == "__main__":
    audio_file = MediaFileFactory.create_media_file(
        media_type=MediaType.AUDIO,
        file_path="audio/song.mp3",
        storage_type=StorageType.S3
    )

    audio_file.download("/tmp/song.mp3")
    audio_file.convert_bitrate(345)
    print(audio_file)

    video_file = MediaFileFactory.create_media_file(
        media_type=MediaType.VIDEO,
        file_path="video/movie.mp4",
        storage_type=StorageType.LOCAL
    )
    video_file.change_video_format("4:3")
    video_file.upload("/tmp/movie.mp4")
    print(video_file)

    photo_file = MediaFileFactory.create_media_file(
        media_type=MediaType.PHOTO,
        file_path="photo/photo.jpg",
        storage_type=StorageType.REMOTE_SERVER
    )

    photo_file.set_filter(filter_name="sepia")
    print(photo_file)
    photo_file.delete()
