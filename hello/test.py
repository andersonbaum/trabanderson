from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///C:/Users/Anderson/Google%20Drive/Estudo/Programa%C3%A7%C3%A3o/Python/trabanderson/hello/templates/index.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("nome").clear()
        driver.find_element_by_name("nome").send_keys("Anderson")
        driver.find_element_by_name("sobrenome").clear()
        driver.find_element_by_name("sobrenome").send_keys("Barbosa")
        driver.find_element_by_name("dia").clear()
        driver.find_element_by_name("dia").send_keys("26")
        driver.find_element_by_name("mes").clear()
        driver.find_element_by_name("mes").send_keys("08")
        driver.find_element_by_name("ano").clear()
        driver.find_element_by_name("ano").send_keys("1985")
        driver.find_element_by_name("rg").clear()
        driver.find_element_by_name("rg").send_keys("00000000")
        driver.find_element_by_name("cpf").clear()
        driver.find_element_by_name("cpf").send_keys("000000000")
        driver.find_element_by_name("cpf2").clear()
        driver.find_element_by_name("cpf2").send_keys("00")
        driver.find_element_by_name("rua").clear()
        driver.find_element_by_name("rua").send_keys("Rua xxx")
        driver.find_element_by_name("numero").clear()
        driver.find_element_by_name("numero").send_keys("123")
        driver.find_element_by_name("bairro").clear()
        driver.find_element_by_name("bairro").send_keys("Nonoai")
        Select(driver.find_element_by_name("estado")).select_by_visible_text("Rio Grande do Sul")
        driver.find_element_by_name("cidade").clear()
        driver.find_element_by_name("cidade").send_keys("Porto Alegre")
        driver.find_element_by_name("cep").clear()
        driver.find_element_by_name("cep").send_keys("91720")
        driver.find_element_by_name("cep2").clear()
        driver.find_element_by_name("cep2").send_keys("000")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("anderson.baum@gmail.com")
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("aaa")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("aaa")
        driver.find_element_by_name("passconfirm").clear()
        driver.find_element_by_name("passconfirm").send_keys("aaa")
        driver.find_element_by_xpath("//input[@value='Limpar']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            # noinspection PyDeprecation
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            # noinspection PyDeprecation
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
