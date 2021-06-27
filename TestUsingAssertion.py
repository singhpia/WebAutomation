from selenium import webdriver

#instantiate the chrome webdriver
driver = webdriver.Chrome()

#request to navigate to google.com
driver.get("https://google.com")

#testing if the title of the page is Google and using try, except just to handle exception
assert driver.title=="Google"
try:
    if driver.title == "Google":
        assert True
except: raise AssertionError

