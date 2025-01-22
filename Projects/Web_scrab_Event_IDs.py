from bs4 import BeautifulSoup
import requests
import json


url = "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
#x = soup.select(id_="container-center")

table_of_contents = soup.table



events = {}
index = 0
table_rows = table_of_contents.find_all("tr")
for tr in table_rows:
    for i, td in enumerate(tr.find_all("td")):
        
        if i == 1:
            data = td.text.strip()
            events[data] = {}
            
        elif i == 2:
            events[data]["Name"] = td.text.strip()
            
            
for key in events.keys():
    print(key)
    description = requests.get("https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=" + key)
    print(description.status_code)
    description_soup = BeautifulSoup(description.text, "html.parser")
    description_paragraphs = description_soup.find_all('p')
    events[key]["Description"] = description_paragraphs[2].text


with open('sysmon-Events-IDs.json', 'w') as file:
    json.dump(events, file)


