import threading

import openai
import pyttsx3
import speech_recognition as sr
import pyaudio
from listenCommand import listen_for_voice_command
from getRespons import get_response_from_openai
from speakrespons import speak_response
from Webbrowser import run_selenium_driver
openai.api_key = "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"




print("hello")


def main():
    is_selenium_running = False
    while True:
        if not is_selenium_running:
            command = listen_for_voice_command()
            if command:
                prompt = (f"{command} ")
                print(prompt)
                response = get_response_from_openai(prompt)
                print(response)
                speak_response(response)
                if "go to" in prompt.lower():
                    run_selenium_driver(prompt.split("go to ")[1])
                    is_selenium_running = True
        else:
            # Wait for user to say "Jenny" to stop using the Selenium driver and go back to the voice assistant
            command = listen_for_voice_command()
            if command and "jenny" in command.lower():
                is_selenium_running = False

                prompt = (f"{command} ")
                print(prompt)
                response = get_response_from_openai(prompt)
                print(response)
                speak_response(response)



main()