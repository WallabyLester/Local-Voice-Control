import sounddevice as sd
import tempfile
import wave

def recording_callback(indata, frames, time, status):
    """ Place 5 second audio chunk in temp file."""
    if status:
        print(status)
    # Create tempfile, with autodeletion
    with tempfile.NamedTemporaryFile(delete=True, suffix='.wav', prefix='audio_', dir='.') as tmpfile:
        # save 5 second audio to .wav file
        with wave.open(tmpfile.name, 'wb') as wave_file:
            wave_file.setnchannels(1) # mono audio
            wave_file.setsampwidth(2) # 16-bit audio
            wave_file.setframerate(16000)   # sample rate
            wave_file.writeframes(indata)

if __name__=="__main__":
    try:
        # 5 second chunks of audio
        with sd.InputStream(callback=recording_callback, dtype='int16', channels=1, samplerate=16000, blocksize=16000*5):
            print("Recording...Press Ctrl+C to stop.")
            while True:
                pass
    except KeyboardInterrupt:
        print("Recording stopped.")
