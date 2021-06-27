from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://goindigo.in")
driver.maximize_window()
time.sleep(6)
driver.find_element_by_xpath("//input[@type='text' and @class='form-control or-src-city']").click()
driver.find_element_by_xpath("(//div[@class='airport-city'][contains(.,'Kolkata, India')])[1]").click()
#driver.find_element_by_xpath("//input[@type='text'][@class='form-control or-dest-city parsley-success']").click()
driver.find_element_by_xpath("(//div[@class='airport-city'][contains(.,'Hyderabad, India')])[3]").click()
driver.find_element_by_xpath("(//input[contains(@data-parsley-required-message,'Please select a valid date')])[1]")
element = driver.find_element_by_xpath("(//a[contains(.,'5')])[1]")
#using jscript to click on the element
driver.execute_script("$(arguments[0]).click();", element)
#using external wait for the element to become clickable
btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary block bold ig-search-btn ig-common-cta addLoader'][@Type = 'submit']")))
btn.submit()
time.sleep(500)
elem1 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "(//img[@src='//static.goindigo.in/content/dam/indigov2/6e-website/homepage/header-logo/icIndigoLogoBlueR-new.svg'])[1]")))
print(elem1)

#performing a context click using action chains
act = ActionChains(driver)
act.context_click()
