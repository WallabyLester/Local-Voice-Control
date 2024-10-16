import sounddevice as sd
from rt_audio_to_text import RTAudioToText


if __name__=="__main__":
    rt_model = RTAudioToText()
    try:
        # 5 second chunks of audio
        with sd.InputStream(callback=rt_model.recording_callback, dtype='int16', channels=1, samplerate=16000, blocksize=16000*5):
            print("Recording...Press Ctrl+C to stop.")
            while True:
                pass
    except KeyboardInterrupt:
        print("Recording stopped.")