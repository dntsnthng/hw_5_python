import os.path



from selene import browser, be, have, command


def test_web():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').set_value("Dima")
    browser.element('#lastName').set_value("Botkin")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').set_value("8800555353")
    browser.element('#userEmail').set_value("sobaka@mail.com")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').send_keys('1991')
    browser.element('.react-datepicker__day--026').click()
    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('l3.jpg'))
    browser.element('#currentAddress').type('usa')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('delhi').press_enter()
    browser.element('#submit').click()

    browser.element('[class="modal-content"]').should(have.text('Dima Botkin'))
    browser.element('[class="modal-content"]').should(have.text('sobaka@mail.com'))
    browser.element('[class="modal-content"]').should(have.text('Male'))
    browser.element('[class="modal-content"]').should(have.text('8800555353'))
    browser.element('[class="modal-content"]').should(have.text('26 January,1991'))
    browser.element('[class="modal-content"]').should(have.text('Math'))
    browser.element('[class="modal-content"]').should(have.text('Sports'))
    browser.element('[class="modal-content"]').should(have.text('l3.jpg'))
    browser.element('[class="modal-content"]').should(have.text('usa'))
    browser.element('[class="modal-content"]').should(have.text('NCR Delhi'))
    browser.element('[class="modal-content"]').should(have.text('Thanks for submitting the form'))

















