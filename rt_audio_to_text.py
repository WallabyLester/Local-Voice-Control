import tempfile
import wave
import whisper 

class RTAudioToText:
    def __init__(self):
        # load the tiny model from Whisper
        self.model = whisper.load_model("tiny")

    def recording_callback(self, indata, frames, time, status):
        """ Place 5 second audio chunk in temp file."""
        if status:
            print(status)
        # Create tempfile, with autodeletion
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix='audio_', dir='.') as tmpfile:
            # save 5 second audio to .wav file
            with wave.open(tmpfile.name, 'wb') as wave_file:
                wave_file.setnchannels(1) # mono audio
                wave_file.setsampwidth(2) # 16-bit audio
                wave_file.setframerate(16000)   # sample rate
                wave_file.writeframes(indata)



