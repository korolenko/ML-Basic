from homework_04.AudioFile import AudioFile

def read_media_file(file,path):
    print(file.read(path))

def change_media_file(file,path):
    print(file.change(path))

if __name__ == "__main__":
    audio_file_path = '/Users/user/Desktop/test.mp3'
    audio_file = AudioFile(path=audio_file_path, codec='mp3')
    read_media_file(audio_file,audio_file_path)

