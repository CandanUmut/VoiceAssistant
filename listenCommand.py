import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "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 "


def listen_for_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"Error requesting results from Google Speech Recognition service; {e}")
        return None
