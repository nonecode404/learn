from appium_test.capability import driver , NoSuchElementException
def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_code_touname').click()
    driver.find_element_by_id('com.tal.kaoyan:id/login_treaty_checkbox').click()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('15083135786')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('xh1234')

    driver.find_element_by_id('com.tal.kaoyan:id/login_uname_login_btncover').click()

try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userinfo_relativelayout').click()
    login()