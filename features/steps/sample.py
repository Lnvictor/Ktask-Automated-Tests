from time import sleep
from behave import when, then, step, given

from selenium.webdriver.support.ui import WebDriverWait

import ipdb

from helpers.google_login import Google


@given("I access my application on browser")
def access_application_link(self):
    self.driver.get("http://localhost:3000")


@when("I click on Entrar button")
def click_entrar(self):
    sleep(3)
    self.driver.find_element_by_xpath(
        '//*[@id="root"]/div/main/section/div/section/a/button'
    ).click()


@step('Log in with "{email}" google account and "{password}" password')
def fill_google_credentials(self, email: str, password: str):
    #Google(self.driver, email, password)
    ipdb.sset_trace()
    google_button = self.wait.until(
        lambda driver: self.driver.find_element_by_name("googleSignUpButton")
    )
    google_button.click()

#    email_field = self.wait.until(
 #       lambda driver: self.driver.find_element_by_id("identifierId")
  #  )
    #email_field.send_keys(email)
    #next_button = self.driver.find_element_by_class_name("VfPpkd-vQzf8d")
    #next_button.click()
    ipdb.sset_trace()

    # email_field = self.wait.until(
    #     lambda driver: self.driver.find_element_by_id("identifierId")
    # )
    # email_field.send_keys(email)
