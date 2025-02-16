import speech_recognition as sr

def transcribe_audio(audio_file):
    """Transcribes a short audio clip to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "Error connecting to the speech recognition service."

if __name__ == "__main__":
    audio_path = "/content/harvard.wav"  # Replace with your audio file
    transcription = transcribe_audio(audio_path)
    print("Transcription:", transcription)
