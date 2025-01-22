# Written by M7md-5shbh
# it performs simple authentication to GitHub using selenium module
#---------------------------------------------

# importing necessary modules
# you can download it through the terminal/cmd using pip install selenium
from selenium import webdriver

# creating a webdriver instance, you can find the supported drivers by selenium
# on https://pypi.org/project/selenium/ in the drivers section or
# search online for how to configure other browsers if you don't find the one you want
browser = webdriver.Firefox()

# opening the webpage/url we want
browser.get("https://github.com")

# finding the Sign in element, keep in mind that the method: find_element_by_* is
# deprecated and removed, so now you have to use the find element while specifing
# the first parameter which is "by" and the second parameter for the "value" you're
# looking for
signin_link = browser.find_element("link text", "Sign in")

# simulating a click on the element we  found
signin_link.click()

# finding the username/password fields using their IDs which you can find in the
# html source code of the page
username_field = browser.find_element("id", "login_field")
password_field = browser.find_element("id", "password")

# the send_keys method simulates typing or sending values to the element specified
username_field.send_keys("myusername")
password_field.send_keys("mypassword")

# submitting the login form
password_field.submit()
# you can also use the username_field.submit(), works the same
