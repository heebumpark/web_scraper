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
  place = []
  title = []
  time = []
  pay = []
  date = []
  company_website = requests.get(URL)
  company_soup = BeautifulSoup(company_website.text, "html.parser")

  informations = company_soup.find("div", {"id" : "NormalInfo"}).find("table").find("tbody").find_all("tr")

  for information in informations:
    
    info_place = information.find("td",{"class":"local"})
    info_title = information.find("span",{"class":"company"})
    info_time = information.find("td", {"class":"data"})
    info_pay = information.find("td",{"class": "pay"})
    info_date = information.find("td",{"class":"regDate"})
    

    if info_place == None:
      continue

    place.append(info_place.text)
    title.append(info_title.text)
    time.append(info_time.text)
    pay.append(info_pay.text)
    date.append(info_date.text)
   

    #print(f"장소 : {info_place.text}, 제목 : {info_title.text}, 시간 : {info_time}, 돈 : {info_pay.text}, 몇분전 : {info_date.text} ")
  print()
  print()
  print()
  print()
  print()
  print(f"----------{name}----------")
  for i in range(len(place)):
    print(f"{place[i]},     {title[i]},     {time[i]},      {pay[i]},    {date[i]} ")
