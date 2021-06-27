from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")
assert driver.title=="Google"
try:
    if driver.title == "Google":
        assert True
except: raise AssertionError

