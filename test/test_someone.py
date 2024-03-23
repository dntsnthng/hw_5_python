import os.path
import time

import pytest
from selene import browser, be, have, command
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_web():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').set_value("Dima").press_tab()
    browser.element('#lastName').set_value("Botkin").press_tab()
    browser.element('#userEmail').set_value("sobaka@mail.com").press_tab()
    browser.element('#userNumber').set_value("88005553535")
    browser.element('[for="hobbies-checkbox-1"]').double_click()
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#subjectsInput').type('Math').press_tab()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').send_keys('1991')
    browser.element('.react-datepicker__day--026').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').type('usa').press_tab()
    browser.element('#react-select-3-input').type('NCR').press_tab()
    browser.element('#react-select-4-input').type('delhi').press_tab()
    browser.element('#uploadPicture').send_keys(os.path.abspath('l3.jpg'))
    browser.element('#submit').click()

    browser.element('[class="modal-content"]').should(have.text('Dima Botkin'))

















