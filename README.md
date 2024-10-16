# Local-Voice-Control
Simple interface that runs Open AI Whisper locally, records audio in real-time, and displays transcribed text. 

Uses Pygame to display real time audio transcription. Takes 2 second samples when pressing the `SPACE` key.
Uses Open AI Whisper to transcribe audio files. Sounddevice is used to record 
temporary audio files in `.wav` format.

To install required libraries:
```
pip install sounddevice
pip install openai-whisper
pip install pygame
```

Launch the Pygame example or import the implementations from `rt_audio_to_text.py` instead.
```
python run_transcription.py
```