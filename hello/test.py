# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re


class test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "https://trabanderson.herokuapp.com/")
        self.selenium.start()

    def test_test(self):
        sel = self.selenium
        sel.open("/")
        sel.type("name=nome", "Anderson")
        sel.type("name=sobrenome", "Barbosa")
        sel.type("name=dia", "26")
        sel.type("name=mes", "08")
        sel.type("name=ano", "1985")
        sel.type("name=rg", "8087")
        sel.type("name=cpf", "000")
        sel.type("name=cpf2", "00")
        sel.type("name=rua", "Rua")
        sel.type("name=numero", "123")
        sel.type("name=bairro", "Nonoai")
        sel.select("name=estado", "label=Rio de Janeiro")
        sel.select("name=estado", "label=Rio Grande do Norte")
        sel.select("name=estado", u"label=Rondônia")
        sel.select("name=estado", "label=Rio Grande do Norte")
        sel.select("name=estado", u"label=Rondônia")
        sel.select("name=estado", "label=Rio Grande do Norte")
        sel.select("name=estado", "label=Rio de Janeiro")
        sel.select("name=estado", u"label=Piauí")
        sel.select("name=estado", "label=Rio de Janeiro")
        sel.select("name=estado", "label=Rio Grande do Norte")
        sel.select("name=estado", u"label=Rondônia")
        sel.select("name=estado", "label=Rio Grande do Sul")
        sel.select("name=estado", "label=Roraima")
        sel.select("name=estado", "label=Rio Grande do Sul")
        sel.type("name=cidade", "Porto Alegre")
        sel.type("name=cep", "9172")
        sel.type("name=cep2", "0")
        sel.type("name=email", "anderson.baum@gmail.com")
        sel.type("name=login", "aaa")
        sel.type("name=pass", "aaa")
        sel.type("name=passconfirm", "aaa")
        sel.click("//input[@value='Limpar']")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
