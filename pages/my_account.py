class MyAccount:
    def __init__(self, driver, wait) -> None:
        self.driver = driver
        self.wait = wait
        self.create_todolist = self.wait.until(lambda driver: self.driver.find_element_by_class_name("Button_button__1OHuF"))
        # self.logout_button = slef

    
    def create_project(self, name: str, desc: str, data: str) -> bool:
        self.create_todolist.click()
        name_field = self.wait.until(lambda driver: self.driver.find_element_by_id("name"))
        name_field.send_keys(name)
        desc_field = self.driver.find_element_by_id("description")
        desc_field.send_keys(desc)
        deadline_field = self.driver.find_element_by_id("deadline")
        deadline_field.send_keys(data)
        self.driver.find_element_by_class_name("Button_button__1OHuF").click()
        
