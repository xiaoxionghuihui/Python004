from selenium import webdriver
import time

try:
    url = 'https://processon.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/header/ul/li[5]/a').click()
    browser.find_element_by_xpath('//*[@id="login_email"]').send_keys('13880852644')
    browser.find_element_by_xpath('//*[@id="login_password"]').send_keys('123456')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()
    time.sleep(5)

except Exception as e:
    print(e)

finally:
    browser.close()
