# created by M7md-5shbh
# it performs scrabbing of stackoverflow newest questions page grabbing basic information like question name and the votes on it
#---------------------------------------------

# importing necessary modules
# you can download them from terminal/cmd using
# pip install requests bs4
import requests
from bs4 import BeautifulSoup

# setting some global parameters
page = 1
count = 0

# performing a get request to stackoverflow
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")

#pages = soup.select(".s-pagination site1 themed pager float-left")

while page < 6:
    print("Page number is ", soup.find(class_="s-pagination--item is-selected").get_text())
    for question in questions:
        count += 1
        print("question ", count)
        print(question.select_one(".s-link").get_text())
        print("votes", question.select_one(".s-post-summary--stats-item-number").get_text())

    next_page = requests.get("https://stackoverflow.com/questions?tab=newest&page=" + str(page))
    questions = soup.select(".s-post-summary")
    page += 1





