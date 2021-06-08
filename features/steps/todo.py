from time import sleep

import ipdb
from behave import given, step, then, when

from pages.my_account import MyAccount


@step("I click on viewTodos")
def click_on_view_todos(self):
    my_account = MyAccount(self.driver, self.wait)
    proj = my_account.todolists[0]
    buttons = proj.find_elements_by_tag_name("button")
    list(filter(lambda b: b.get_attribute("data-tip") == "Acessar toDos", buttons))[
        0
    ].click()


@then("Click on create todo button")
def click_on_create_todo_button(self):
    btn = self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[1]/button'
        )
    )
    btn.click()


@step("I create a todo with the following data")
def create_todo(self):
    table = {row["Name"]: row["Value"] for row in self.table}
    name_field = self.wait.until(lambda driver: self.driver.find_element_by_id("name"))
    name_field.send_keys(table["nome"])
    desc_field = self.driver.find_element_by_id("description")
    desc_field.send_keys(table["desc"])
    deadline_field = self.driver.find_element_by_id("deadline")
    deadline_field.send_keys(table["data"])

    sleep(1)
    self.driver.find_element_by_xpath(
        '//*[@id="ModalView"]/div/div/section/form/button'
    ).click()
    sleep(4)


@then('the "{todo_name}" todo should be exists on "{session}" session')
def verify_todo_creation(self, todo_name: str, session: str):
    sleep(4)
    session_element = self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[1]'
        )
    )

    if session == "Em andamento":
        session_element = self.wait.until(
            lambda driver: self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[2]'
            )
        )
    elif session == "Concluido":
        session_element = self.wait.until(
            lambda driver: self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[3]'
            )
        )

    titles = [title.text for title in session_element.find_elements_by_tag_name("h3")]
    assert todo_name.upper() in titles


@then("Click to edit todo")
def click_on_edit_todo(self):
    self.wait.until(
        lambda driver: driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[1]/ul/li/div[2]/button[1]'
        )
    ).click()


@then('I change status to "{status}"')
def change_status(self, status: str):
    sleep(4)
    if status == "Em andamento":
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[1]/ul/li[1]/div[1]/button'
        ).click()
    elif status == "Concluido":
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[2]/div[2]/ul/li/div[1]/button[2]'
        ).click()


@then("foo")
def _(self):
    ipdb.sset_trace()
