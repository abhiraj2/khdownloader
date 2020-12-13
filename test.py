from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyrobot
import pyautogui
import time


# getting to the form
robot = pyrobot.Robot()
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.playstation.com/en-in/support/contact-us/contact-form/")
time.sleep(5)
select1 = Select(browser.find_element_by_id("contact_us_type_select"))
time.sleep(0.5)
select1.select_by_visible_text("PlayStation Store refunds and cancellations")
time.sleep(2)

# accepting cookies
browser.find_element_by_id("_evidon-accept-button").click()
browser.find_element_by_id("js-SIEWS1lib-header-CloseIcon").click()
time.sleep(2)
# form filling area
name_area = browser.find_element_by_id("field_4")
name_area.send_keys("Abhiraj Singh")
online_id_area = browser.find_element_by_id("field_5")
online_id_area.send_keys("blundr_strike")
contact_email_address = browser.find_element_by_id("field_6")
contact_email_address.send_keys("abhiraj.official15@gmail.com")
sign_in_email = browser.find_element_by_id("field_7")
sign_in_email.send_keys("abhiraj.official15@gmail.com")
browser.find_element_by_id("field_9_1").click()
content_name = browser.find_element_by_id("field_10")
content_name.send_keys("Cyberpunk 2077")

Select(browser.find_element_by_id("field_11")).select_by_visible_text("The content isn't working properly")


add_info = browser.find_element_by_id("field_14")
add_info.click()
time.sleep(2)
date_picker = browser.find_element_by_id("field_12")
pyautogui.click(430, 735)
time.sleep(0.5)
pyautogui.click(430, 735)
time.sleep(0.2)
browser.find_element_by_tag_name('body').send_keys('07122020')
transac_id = browser.find_element_by_id('field_13')
transac_id.send_keys('234814230261')
add_info.send_keys('The game is completely broken and is plagued with massive game breaking visual and gameplay bugs, '
                   'that have already caused my PS4 to crash multiple times(more than 12) and it happens every half '
                   'an hour or so. I have already tried to contact you guys regarding this issue but there has been '
                   'no contact from your end, which is very disappointing. Please help in getting my money back and '
                   'returning this BROKEN product.')

time.sleep(0.5)
browser.find_element_by_class_name('cta__primary').click()
time.sleep(5)
browser.close()
