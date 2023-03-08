import pyttsx3
def speak_response(response):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id )
    engine.say(response)
    engine.runAndWait()
    # 'com.apple.speech.synthesis.voice.samantha'