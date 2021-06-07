from time import sleep

from behave import given, step, then, when
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from helpers.default_login import make_login
from pages.my_account import MyAccount


@given("I access my application on browser")
def access_application_link(self):
    self.driver.get("http://localhost:3000")


@when("I click on Entrar button")
def click_entrar(self):
    self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div[2]/a/button'
        )
    ).click()


@step('Log in with "{email}" account and "{password}" password')
def default_login(self, email: str, password: str) -> None:
    make_login(self.driver, self.wait, email, password)


@then("I logout")
def logout(self):
    self.wait.until(lambda driver: driver.find_element_by_id("logout")).click()
    self.driver.get("http://localhost:3000")


@given("I see my homepage")
def _(self):
    element = self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/h1[1]'
        )
    )
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
    assert project_name.upper() == my_account.todolist.text


@then('I see a error message with "{message}" on "{mode}" modal')
def check_error_message(self, message: str, mode: str):
    sleep(2)
    types = {"create": "modalCreate", "createTodo": "ModalView", "edit": "ModalAdd"}

    try:
        error_msg = self.driver.find_element_by_xpath(
            f'//*[@id="{types[mode]}"]/div/div/section/form/p'
        )
        assert error_msg.text == message
    except NoSuchElementException as e:
        error_message_name = self.driver.find_element_by_xpath(
            f'//*[@id="{types[mode]}"]/div/div/section/form/div[1]/p'
        )
        error_message_desc = self.driver.find_element_by_xpath(
            f'//*[@id="{types[mode]}"]/div/div/section/form/div[2]/p'
        )
        error_message_deadline = self.driver.find_element_by_xpath(
            f'//*[@id="{types[mode]}"]/div/div/section/form/div[3]/div/p'
        )

        assert error_message_name.text == "Preencha o campo."
        assert error_message_desc.text == "Preencha o campo."
        assert error_message_deadline.text == "Preencha o campo."


@then('I click to edit project called "{project_name}"')
def click_to_edit_project(self, project_name):
    my_account = MyAccount(self.driver, self.wait)
    proj = my_account.todolist
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
    self.driver.find_element_by_xpath(
        '//*[@id="ModalAdd"]/div/div/section/div/button'
    ).click()
    name_field = self.driver.find_element_by_id("name")
    desc_field = self.driver.find_element_by_id("description")
    deadline_field = self.driver.find_element_by_id("deadline")
    save_button = self.driver.find_element_by_xpath(
        '//*[@id="ModalAdd"]/div/div/section/form/div[4]/button[1]'
    )

    name_field.send_keys(table["name"])
    desc_field.send_keys(table["desc"])
    deadline_field.send_keys(table["data"])
    save_button.click()


@then('I add user "{email}" to the project')
def click_on_access_button(self, email: str):
    btn = self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            "//*[@id='root']/div/main/section/div/section/div/div[2]/div/div/ul/li/div[2]/div[1]/button"
        )
    )
    btn.click()
    email_field = self.driver.find_element_by_id("email")
    email_field.send_keys(email)
    add_button = self.driver.find_element_by_xpath(
        '//*[@id="ModalAddUser"]/div/div/section/form/div[2]/button[1]'
    )
    add_button.click()

    if "@" in email:
        message = self.wait.until(
            lambda driver: self.driver.find_element_by_xpath(
                '//*[@id="ModalAddUser"]/div/div/section/form/p'
            )
        )
        assert message.text == "Usuário foi adicionado com sucesso!"
        return

    paragraphs = self.wait.until(lambda driver: driver.find_elements_by_tag_name("p"))
    assert "Email inválido" in [message.text for message in paragraphs]


@then('I remove user "{email}" from project"')
def remove_user_from_project(self, email: str):
    self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            "//*[@id='root']/div/main/section/div/section/div/div[2]/div/div/ul/li/div[2]/div[1]/button"
        )
    ).click()

    btn = self.driver.find_element_by_xpath(
        '//*[@id="ModalAddUser"]/div/div/section/form/div[2]/button[2]'
    )
    btn.click()
    self.driver.find_element_by_id("email").send_keys(email)
    self.driver.find_element_by_xpath(
        '//*[@id="ModalAddUser"]/div/div/section/form/div[2]/button[1]'
    ).click()

    message = self.wait.until(
        lambda driver: self.driver.find_element_by_xpath(
            "//*[@id='ModalAddUser']/div/div/section/form/p"
        )
    )
    assert message.text == "Usuário foi removido com sucesso"
