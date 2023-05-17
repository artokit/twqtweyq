import time

import requests
from bs4 import BeautifulSoup
from anticaptchaofficial.imagecaptcha import *
import base64
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome

solver = imagecaptcha()
solver.set_verbose(1)
token = '7b1afb5ba3b9e9fe26a24e182583d95e'
solver.set_key(token)
session = requests.Session()
username = 'artokit1dwr'
password = 'AijqlkKmoiInwr51'


def check_start_captcha(driver):
    driver.get('https://in-k2web.at/')
    while True:
        captcha_elem = driver.find_elements(By.CSS_SELECTOR, '#captcha-img')

        if not captcha_elem:
            return

        captcha_elem = captcha_elem[0]

        src = captcha_elem.get_attribute('src')
        photo = base64.b64decode(src.replace('data:image/png;base64,  ', ''))

        with open('cap.png', 'wb') as f:
            f.write(photo)

        res = send_captcha()
        driver.find_element(By.CSS_SELECTOR, '.login-input').send_keys(res)
        driver.find_element(By.CSS_SELECTOR, '.button-submit').click()


def login(driver: Chrome):
    global username, password
    while True:
        captcha_elem = driver.find_elements(By.CSS_SELECTOR, '.captcha img')

        if not captcha_elem:
            return

        captcha_elem = captcha_elem[0]

        username_input, password_input, captcha_input = driver.find_elements(By.CSS_SELECTOR, '.login-input')[:3]

        for elem in (username_input, password_input, captcha_input): elem.clear()

        username_input.send_keys(username)
        password_input.send_keys(password)

        src = captcha_elem.get_attribute('src')
        photo = base64.b64decode(src.replace('data:image/jpeg;charset=utf-8;base64, ', ''))

        with open('cap.png', 'wb') as f:
            f.write(photo)

        res = send_captcha()
        captcha_input.send_keys(res)

        driver.find_element(By.CSS_SELECTOR, '.button-submit').click()


def get_cookies():
    driver = Chrome()
    check_start_captcha(driver)
    login(driver)
    time.sleep(10)
    return driver.get_cookies()

# captcha_text = solver.solve_and_return_solution("cap.jpeg")
# print(captcha_text)
# if captcha_text != 0:
#     print("captcha text " + captcha_text)
# else:
#     print("task finished with error " + solver.error_code)


def send_captcha():
    while True:
        captcha_text = solver.solve_and_return_solution("cap.png")
        if captcha_text != 0:
            return captcha_text


# def check_start_captcha(content: bytes):
#     bs = BeautifulSoup(content)
#     user_id = bs.select_one('form input').get('value')
#     print(user_id)
#     captcha = bs.select('#captcha-img')
#
#     if not captcha:
#         print('wrq')
#         return
#
#     src = captcha[0].get('src')
#     photo = base64.b64decode(src.replace('data:image/png;base64,  ', ''))
#     photo = session.get(src).content
    # with open('cap.png', 'wb') as f:
    #     f.write(photo)
    #
    # res = send_captcha()
    # print(res)
    # p = session.post(
    #     'https://in-k2web.at/',
    #     data={'user-ld': user_id, 'sfill': res}
    # )

    # f = open('w.html', 'wb')
    # f.write(p.content)
    # f.close()
    # input('check')


# while True:
#     r = session.get('https://in-k2web.at/')
#     check_start_captcha(r.content)
#     print('tq')
cookies = get_cookies()
print(cookies)
