from advanced_audio_player import AdvancedAudioPlayer
from audio_player_adapter import AdvancedAudioPlayerAdapter

advanced_player = AdvancedAudioPlayer()

adapter = AdvancedAudioPlayerAdapter(advanced_player)

adapter.play("mp3", "song.mp3")
adapter.play("wav", "sound.wav")
