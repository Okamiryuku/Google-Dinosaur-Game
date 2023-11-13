import pyautogui
from selenium import webdriver
import time


def game():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://elgoog.im/dinosaur-game/")
    driver.maximize_window()

    time.sleep(3)

    pyautogui.press('space')

    try:
        while True:
            screenshot = pyautogui.screenshot()

            if screenshot.getpixel((600, 850)) == (83, 83, 83):
                pyautogui.press('space')

    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()


game()
