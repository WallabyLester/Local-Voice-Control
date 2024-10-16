import sounddevice as sd
from rt_audio_to_text import RTAudioToText


if __name__=="__main__":
    rt_model = RTAudioToText()
    fs = 16000
    duration = 2    # 2 second chunks of audio

    with sd.InputStream(callback=rt_model.recording_callback, dtype='int16', channels=1, samplerate=fs, blocksize=fs*duration):
        print("Recording...")
        sd.sleep(duration * 1000) # in ms
    
    print(rt_model.output)