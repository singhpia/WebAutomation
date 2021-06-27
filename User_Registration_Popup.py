from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities
import re


st = "I am Priya Tink, whatever, you got me!"
r = re.compile(r'ti\s')
match = r.search(st)
for m in match:
    print(m)
print("match is", match)

# driver = webdriver.Chrome()
# f = DC.CHROME()
option = webdriver.ChromeOptions()
option.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options=option)
fox = webdriver.FirefoxProfile()
fox.accept_untrusted_certs(True)
#f.get("http://automationpractice.com/index.php")
driver.set_page_load_timeout(5)
driver.maximize_window()
current_win = driver.current_window_handle
signIn = driver.find_element_by_xpath("//a[@class='login']").click()
create_email = driver.find_element_by_id("email_create")
a = 'alkjkkf@ty.com'
create_email.send_keys(a)
btnSubmit = driver.find_element_by_id("SubmitCreate").click()
driver.implicitly_wait(5)
# radio_mrs = driver.find_element_by_xpath("//div[@id='uniform-id_gender1']/span/input[@id='id_gender1']")
radio_mrs = driver.find_element_by_xpath("//*[@id= 'id_gender1']")
wt = WebDriverWait(driver, 4)
wt.until(EC.element_to_be_clickable((By.XPATH, "//*[@id= 'id_gender1']")))
radio_mrs.click()
first_name = driver.find_element_by_id("customer_firstname").send_keys("fu")
last_name = driver.find_element_by_id("customer_lastname").send_keys("l")
#email = driver.find_element_by_id("email").send_keys("3@u.com")
pwd = driver.find_element_by_id("passwd").send_keys("125890")
date = Select(driver.find_element_by_id("days"))
date.select_by_index(28)
month = Select(driver.find_element_by_id("months"))
month.select_by_index(5)
year = Select(driver.find_element_by_id("years"))
year.select_by_value("2019")
if year.is_multiple:
    print("Its multi select box")
elif year.is_multiple == None:
    print("None")
else:
    print("Nothing")
# checkbox_receive = driver.find_element_by_id("optin").send_keys(Keys.ENTER)

fn = driver.find_element_by_id("firstname").send_keys("FN")
ln = driver.find_element_by_id("lastname").send_keys("LN")
add = driver.find_element_by_id("address1").send_keys("45, Sarjap road, benagaluru")
city = driver.find_element_by_id("city").send_keys("Bengaluru")
state = Select(driver.find_element_by_id("id_state"))
state.select_by_index(4)
pin = driver.find_element_by_id("postcode").send_keys("56490")
cntry = Select(driver.find_element_by_id("id_country")).select_by_value("21")
phone = driver.find_element_by_id("phone_mobile")
phone.send_keys("1234567899")
print('myphn',phone)
alias = driver.find_element_by_id("alias")
alias.clear()
alias.send_keys("alia")
btnSubmitform = driver.find_element_by_id("submitAccount")
btnSubmitform.submit()
print("Wow")
win2 = driver.current_window_handle
if current_win == win2:
    print("this is a different window")

