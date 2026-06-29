from faster_whisper import WhisperModel
model = WhisperModel('base', device="cpu")
segments, info = model.transcribe("LLM.m4a")
for segment in segments:
    print(segment.text)