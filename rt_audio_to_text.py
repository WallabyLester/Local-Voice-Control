import tempfile
import wave
import whisper 

class RTAudioToText:
    """ Real-time audio to text transcription class. 

    Uses Open AI Whisper locally to transcribe audio files.

    ...

    Methods
    -------
    transcribe_to_text(input_file):
        Run transcription on audio file.
    recording_callback(indata, frames, time, status):
        Write audio to temporary file.
    """
    def __init__(self):
        """ Constructs Whisper CPU model and initialized output.
        """
        self.model = whisper.load_model("tiny", device="cpu")
        self.output = None

    def transcribe_to_text(self, input_file):
        """ Transcribes audio file to text using Whisper CPU.

        Parameters
        ----------
        input_file : String
                Path to the audio file. 

        Returns
        -------
        String result of transcription.
        """
        print("Running whisper transcription...")
        result = self.model.transcribe(input_file, fp16=False)
        
        return result["text"]

    def recording_callback(self, indata, frames, time, status):
        """ Callback for sounddevice input stream. Creates temporary file. 
     
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

        with tempfile.NamedTemporaryFile(delete=True, suffix='.wav', prefix='audio_', dir='.') as tmpfile:
            with wave.open(tmpfile.name, 'wb') as wave_file:
                wave_file.setnchannels(1)       # mono audio
                wave_file.setsampwidth(2)       # 16-bit audio
                wave_file.setframerate(16000)   # sample rate
                wave_file.writeframes(indata)

            self.output = self.transcribe_to_text(tmpfile.name)
            