import sounddevice as sd
import tempfile
import wave

def recording_callback(indata, frames, time, status):
    """ Callback for sounddevice input stream. 
     
    Parameters
    ----------
        indata : numpy.ndarray
            Input audio.
        frames : int
            Frames in audio data.
        time : CData
            Current stream time.
        status : CallbackFlags
            Callback status.
    """
    if status:
        print(status)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix='audio_', dir='.') as tmpfile:
        with wave.open(tmpfile.name, 'wb') as wave_file:
            wave_file.setnchannels(1)       # mono audio
            wave_file.setsampwidth(2)       # 16-bit audio
            wave_file.setframerate(16000)   # sample rate
            wave_file.writeframes(indata)

if __name__=="__main__":
    try:
        with sd.InputStream(callback=recording_callback, dtype='int16', channels=1, samplerate=16000, blocksize=16000*5):
            print("Recording...Press Ctrl+C to stop.")
            while True:
                pass
    except KeyboardInterrupt:
        print("Recording stopped.")
