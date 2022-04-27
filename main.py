import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

website_result = requests.get(alba_url)
website_soup = BeautifulSoup(website_result.text, "html.parser")

jobs = website_soup.find("div",{"id": "MainSuperBrand"}).find("ul",{"class": "goodsBox"}).find_all("li", {"class": "impact"})

for job in jobs:
  URL = job.find("a",{"class":"goodsBox-info"})['href']
  name = job.find("span",{"class":"company"}).text

  company_website = requests.get(URL)
  company_soup = BeautifulSoup(company_website.text, "html.parser")

  informations = company_soup.find("div", {"id" : "NormalInfo"}).find("table").find("tbody").find_all("tr")
  file = open(f'{name}.csv', mode="w", encoding='UTF-8')
  writer = csv.writer(file)

  writer.writerow(["place", "title", "time", "pay", "date"])
  
  for information in informations:
    
    info_place = information.find("td",{"class":"local"})
    info_title = information.find("span",{"class":"company"})
    info_time = information.find("td", {"class":"data"})
    info_pay = information.find("td",{"class": "pay"})
    info_date = information.find("td",{"class":"regDate"})
    
    if info_place == None:
      continue
    data = []

    data.append(info_place.text)
    data.append(info_title.text)
    data.append(info_time.text)
    data.append(info_pay.text)
    data.append(info_date.text)
    writer.writerow(data)


