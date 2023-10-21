from audio_player import AudioPlayer

class AdvancedAudioPlayerAdapter(AudioPlayer):
    def __init__(self, advanced_player):
        self.advanced_player = advanced_player

    def play(self, audio_type, filename):
        if audio_type == "mp3":
            self.advanced_player.play_mp3(filename)
        elif audio_type == "wav":
            self.advanced_player.play_wav(filename)
        else:
            print(f"Unsupported audio type: {audio_type}")
