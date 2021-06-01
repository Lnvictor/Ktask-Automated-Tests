from time import sleep
from behave import when, then, step, given

from selenium.webdriver.support.ui import WebDriverWait

import ipdb

from pages.my_account import MyAccount


@given("I access my application on browser")
def access_application_link(self):
    self.driver.get("http://localhost:3000")


@when("I click on Entrar button")
def click_entrar(self):
    self.wait.until(
        lambda driver: self.driver.find_element_by_class_name("Button_button__1OHuF")
    ).click()


@step('Log in with "{email}" account and "{password}" password')
def default_login(self, email: str, password: str) -> None:
    email_field = self.wait.until(
        lambda driver: self.driver.find_element_by_id("signInFormUsername")
    )
    email_field.send_keys(email)

    password_field = self.driver.find_element_by_id("signInFormPassword")
    password_field.send_keys(password)

    self.driver.find_element_by_name("signInSubmitButton").click()


@then("devo estar logado")
def _(self):
    element = self.wait.until(
        lambda driver: self.driver.find_element_by_class_name("MyAccount_title__p7ObQ")
    )
    assert element.text == "K-Task gerenciando seus projetos"
    assert self.driver.find_element_by_id("login").text == "Conectado"


@step("crio um todolist com os dados")
def _(self):
    table = {row["Name"]: row["Value"] for row in self.table}
    page = MyAccount(self.driver, self.wait)
    page.create_project(table["nome"], table["desc"], table["data"])
    el = self.wait.until(
        lambda driver: self.driver.find_element_by_class_name(
            "MyAccount_todoList__1oPs"
        )
    )
    assert el.text == "EXEMPLO TODOLIST"
