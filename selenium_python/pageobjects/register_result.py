# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from selenium_tid_python import selenium_driver
from selenium_tid_python.pageobjects.page_object import PageObject
from selenium_tid_python.pageelements.text_page_element import TextPageElement
from selenium_python.pageobjects import locators


class MessageElement(TextPageElement):
    def __init__(self):
        self.locator = locators["register.result.message"]


class RegisterResultPageObject(PageObject):
    message = MessageElement()

    def __init__(self):
        self.driver = selenium_driver.driver