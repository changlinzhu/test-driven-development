from selenium import webdriver

browser = webdriver.Chrome('/Users/zoro/Documents/PycharmProjects/Test-driven-Development/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
