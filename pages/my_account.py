from time import sleep


class MyAccount:
    def __init__(self, driver, wait) -> None:
        self.driver = driver
        self.wait = wait
        self.create_todolist = self.wait.until(
            lambda driver: self.driver.find_element_by_class_name(
                "Button_button__1OHuF"
            )
        )
        self.logout_button = self.driver.find_element_by_id("logout")
        sleep(2)
        self.todolists = self.driver.find_elements_by_class_name(
            "MyAccount_todoList__1_oPs"
        )

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
        self.driver.find_element_by_class_name("Button_button__1OHuF").click()
        sleep(2)
        self.todolists = self.driver.find_elements_by_class_name(
            "MyAccount_todoList__1_oPs"
        )

    def exclude_project(self, desc):
        pass
