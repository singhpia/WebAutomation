from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import SessionNotCreatedException
import openpyxl
import json
import sys


def test_search_book():
    baseurl = "https://leanpub.com/bookstore"
    search_word = input("What do you want to search on LeanPub? Need a keyword to begin with!")
    url = baseurl+"?search="+search_word
    print(sys.version)
    try:
        driver = webdriver.Chrome("C:\\Users\\Prateek.THINKPAD\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
        driver.get(url)
        driver.maximize_window()
    except SessionNotCreatedException:
        print("Browser version not supported")
    results = []
    results = list(driver.find_elements_by_xpath("//li[@class='BookListItem ListItem']"))
    print(results)
    file = open("b.json",'a+')
    a = 1
    for i in results:
        print("{} book result: ".format(a))
        item_rank = i.find_element_by_xpath(".//span[@class='ItemRank']")
        print(item_rank.text)
        title = i.find_element_by_xpath(".//article/h3")
        print(title.text)
        file.writelines(json.dumps(title.text))
        print("file contents -")
        file.read()
        author = i.find_element_by_xpath(".//div[@class='names']/span")
        print(author.text)
        a = a + 1
        test_dict = []
        try:
            book_details = i.find_element_by_xpath("//div[@class='hint']").text
            print(book_details)
            test_dict.append(book_details)
            print("contents in list are - ",test_dict)
        except NoSuchElementException:
            print("No such element found")
        finally:
            print("finally executed")
            print("final content ",test_dict)


    """top10 = {
            {"rank": "# 1"}, {"title": "Composing Software"}, {"author": "Eric Elliott"}}
    json_file = json.dump(top10, indent=5)"""


test_search_book()
        #
        # obj_ref = wmi.WMI()
        # for res in results: