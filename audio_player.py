class AudioPlayer:
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            print(f"Playing MP3 file: {filename}")
        else:
            print(f"Unsupported audio type: {audio_type}")
