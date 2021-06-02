from time import sleep

import ipdb
from behave import given, step, then, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from helpers.default_login import make_login
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
    make_login(self.driver, self.wait, email, password)


@then("I logout")
def logout(self):
    my_account = MyAccount(self.driver, self.wait).logout_button.click()
    self.driver.get("http://localhost:3000")


@given("I see my homepage")
def _(self):
    element = self.wait.until(
        lambda driver: self.driver.find_element_by_class_name("MyAccount_title__p7ObQ")
    )
    assert element.text == "K-Task gerenciando seus projetos"
    assert self.driver.find_element_by_id("login").text == "conectado"


@step("I create a project with the following data")
def _(self):
    table = {row["Name"]: row["Value"] for row in self.table}
    page = MyAccount(self.driver, self.wait)
    page.create_project(table["nome"], table["desc"], table["data"])


@step('there must be a project called "{project_name}"')
def check_project_name(self, project_name):
    sleep(1)
    my_account = MyAccount(self.driver, self.wait)
    assert project_name.upper() in [t.text for t in my_account.todolists]


@then('I see a error message with "{message}"')
def check_error_message(self, message: str):
    error_msg = self.driver.find_element_by_class_name("Error_error__2Um6o")
    assert error_msg.text == message


@then('I click to edit project called "{project_name}"')
def click_to_edit_project(self, project_name):
    my_account = MyAccount(self.driver, self.wait)
    proj = my_account.todolists[0]
    buttons = proj.find_elements_by_tag_name("button")
    list(
        filter(lambda b: b.get_attribute("data-tip") == "Visualizar e editar", buttons)
    )[0].click()


@step("I should see the project edition modal")
def check_edition_modal(self):
    title = self.driver.find_element_by_class_name("title")
    assert title.text == "VISUALIZE SEU PROJETO"


@step("I edit the project with the following data")
def edit_project(self):
    table = {row["Name"]: row["Value"] for row in self.table}
    self.driver.find_element_by_class_name("Button_button__1OHuF").click()
    name_field = self.driver.find_element_by_id("name")
    desc_field = self.driver.find_element_by_id("description")
    deadline_field = self.driver.find_element_by_id("deadline")
    save_button = self.driver.find_elements_by_class_name("Button_button__1OHuF")[0]

    name_field.send_keys(table["name"])
    desc_field.send_keys(table["desc"])
    deadline_field.send_keys(table["data"])
    save_button.click()
