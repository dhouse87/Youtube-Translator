# audio_transcriber.py

from faster_whisper import WhisperModel

def transcribe_audio(audio_path, language=None):
    model = WhisperModel("small", device="cpu", compute_type="int8")  # You can change model size if needed

    if language:
        segments, info = model.transcribe(audio_path, language=language)
    else:
        segments, info = model.transcribe(audio_path)

    full_text = ""
    for segment in segments:
        full_text += segment.text + " "

    print(f"Transcription complete. Detected language: {info.language}")
    return full_text, info.language
