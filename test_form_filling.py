from selene import browser, have, command, by
import os


def test_complete_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Alexandr')
    browser.element('#lastName').type('Yurpolskiy')
    browser.element('#userEmail').type('hirampy@mail.ru')
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').type('9851429399')
    browser.element('#dateOfBirthInput').perform(command.js.click)
    browser.element('.react-datepicker__month-select').click() \
        .element(by.text('December')).click()
    browser.element('.react-datepicker__year-select').click() \
        .element(by.text('1991')).click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').set_value('arts').press_tab() \
        .set_value('maths').press_tab() \
        .set_value('hindi').press_tab()
    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#hobbies-checkbox-2').perform(command.js.click)
    browser.element('#hobbies-checkbox-3').perform(command.js.click)
    browser.element('.form-control-file').send_keys(os.path.abspath('my_photo.png'))
    browser.element('#currentAddress').type('Central Street 55')
    browser.element('#state').click() \
        .element(by.text('NCR')).click()
    browser.element('#city').click() \
        .element(by.text('Delhi')).click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Alexandr Yurpolskiy',
        'hirampy@mail.ru',
        'Male',
        '9851429399',
        '10 December,1991',
        'Arts, Maths, Hindi',
        'Sports, Reading, Music',
        'my_photo.png',
        'Central Street 55',
        'NCR Delhi'
    ))
    browser.element('#closeLargeModal').click()
