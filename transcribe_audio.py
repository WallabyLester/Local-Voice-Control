import whisper 

# load the base model from Whisper
model = whisper.load_model("tiny")

audio = "test_audio.wav"

result = model.transcribe(audio, fp16=False)
print(result["text"])
