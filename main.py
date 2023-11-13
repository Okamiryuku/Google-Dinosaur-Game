import pyautogui
from selenium import webdriver
import time


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.3)
    pyautogui.keyUp('space')


def game():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://elgoog.im/dinosaur-game/")
    driver.maximize_window()

    time.sleep(3)

    jump()

    while True:
        screenshot = pyautogui.screenshot()
        if screenshot.getpixel((600, 850)) == (83, 83, 83):
            jump()


game()
