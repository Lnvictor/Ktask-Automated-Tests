from time import sleep

import ipdb
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait


def make_login(driver: Chrome, wait: WebDriverWait, email: str, password: str):
    wait_2 = WebDriverWait(driver, 15)
    btn = wait_2.until(
        lambda driver: driver.find_element_by_class_name(
            "btn.btn-primary.submitButton-customizable"
        )
    )
    if btn.text == "Sign In as xileyaf341@relumyx.com":
        btn.click()
    else:
        email_field = wait.until(
            lambda driver: driver.find_element_by_id("signInFormUsername")
        )
        email_field.send_keys(email)
        password_field = driver.find_element_by_id("signInFormPassword")
        password_field.send_keys(password)
        driver.find_element_by_name("signInSubmitButton").click()
