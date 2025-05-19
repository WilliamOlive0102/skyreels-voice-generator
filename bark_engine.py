
import torchaudio
from bark import generate_audio, preload_models

preload_models()

def gerar_audio(texto):
    audio_array = generate_audio(texto)
    torchaudio.save("voz.wav", audio_array, 24000)
    return "voz.wav"
