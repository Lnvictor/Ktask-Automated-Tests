from time import sleep


class Google:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.driver.get("https://pt.stackoverflow.com/users/signup?ssrc=head")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(
            password
        )
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
