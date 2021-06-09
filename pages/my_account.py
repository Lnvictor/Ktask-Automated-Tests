from time import sleep

from selenium.common.exceptions import TimeoutException


class MyAccount:
    def __init__(self, driver, wait) -> None:
        self.driver = driver
        self.wait = wait
        self.create_todolist = self.wait.until(
            lambda driver: self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/main/section/div/section/div/div[1]/button'
            )
        )
        self.logout_button = self.driver.find_element_by_id("logout")
        sleep(2)
        try:
            self.todolist = self.wait.until(
                lambda driver: self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/section/div/section/div/div[2]/div/div/ul/li'
                )
            )
        except TimeoutException:
            self.todolist = None

    def create_project(self, name: str, desc: str, data: str):
        self.create_todolist.click()
        name_field = self.wait.until(
            lambda driver: self.driver.find_element_by_id("name")
        )
        name_field.send_keys(name)
        desc_field = self.driver.find_element_by_id("description")
        desc_field.send_keys(desc)
        deadline_field = self.driver.find_element_by_id("deadline")
        deadline_field.send_keys(data)
        self.driver.find_element_by_xpath(
            '//*[@id="modalCreate"]/div/div/section/form/button'
        ).click()
        sleep(4)
        self.todolist = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/section/div/section/div/div[2]/div/div/ul/li'
        )

    def exclude_project(self, desc):
        pass
