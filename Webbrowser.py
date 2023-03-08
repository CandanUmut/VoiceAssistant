from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openai
import pyttsx3
import speech_recognition as sr
import pyaudio
from listenCommand import listen_for_voice_command
from getRespons import get_response_from_openai
from speakrespons import speak_response
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




def run_selenium_driver(prompt):

    driver = webdriver.Chrome(r'C:\Users\umtcn\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.google.com")



    search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
    search_box.send_keys(prompt)
    search_box.send_keys(Keys.ENTER)

    while True:
        try:
            command = listen_for_voice_command()
            if "jenny" in command.lower():
                driver.quit()
                break
            elif "back" in command.lower():
                driver.back()
            elif "forward" in command.lower():
                driver.forward()
            elif "clear" in command.lower():
                search_box.clear()
            elif "search" in command.lower():
                search_box = driver.find_element(By.NAME, "q")
                search_box.send_keys(Keys.RETURN)
            elif "scroll down" in command.lower():
                driver.execute_script("window.scrollBy(0,500)")
            elif "scroll up" in command.lower():
                driver.execute_script("window.scrollBy(0,-500)")
            elif "click" in command.lower():
                results = driver.find_elements(By.XPATH, "//h3")
                if len(results) > 0:
                    results[0].click()
                    time.sleep(2)
            elif "test" in command.lower():
                move_mouse(driver)
            else:
                print("I didnt understand that")



        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    driver.quit()

def move_mouse(driver):
    # Get the size of the window

    # Get the button element by xpath
    button = driver.find_elements(By.XPATH, "//h3")
    if len(button) > 0:
        button[0].click()
        time.sleep(2)


    # Move the mouse to the button
    #     ActionChains(driver).move_to_element(button[0]).perform()


        # Click the button

        window_size = driver.execute_script(
            "return {width: window.innerWidth || document.body.clientWidth, "
            "height: window.innerHeight || document.body.clientHeight};"
        )
        center_x, center_y = window_size["width"] // 2, window_size["height"] // 2
        ActionChains(driver).move_by_offset(center_x - button[0].location["x"], center_y - button[0].location["y"]).perform()
        ActionChains(driver).click(button[0]).perform()
    else:
        print("anlamadim haci nereeee")

    # # Calculate the center of the window
    # center_x, center_y = window_size["width"] // 2, window_size["height"] // 2
    #
    # # Move the mouse to the center of the window
    # ActionChains(driver).move_by_offset(center_x, center_y).perform()
    #
    # # Move the mouse to the top left corner of the window
    # ActionChains(driver).move_by_offset(-center_x, -center_y).perform()
    #
    # # Move the mouse to the top right corner of the window
    # ActionChains(driver).move_by_offset(window_size["width"], 0).perform()
    #
    # # Move the mouse to the bottom right corner of the window
    # ActionChains(driver).move_by_offset(0, window_size["height"]).perform()
    #
    # # Move the mouse to the bottom left corner of the window
    # ActionChains(driver).move_by_offset(-window_size["width"], 0).perform()
    #
    # # Move the mouse back to the center of the window
    # ActionChains(driver).move_by_offset(center_x, center_y).perform()




