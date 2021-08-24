from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

print("""
 _____ _   _  _____  ___  ________  _   _ _____ _____ 
|_   _| | | ||  ___| |  \/  |  _  || | | |_   _|  ___|
  | | | |_| || |__   | .  . | | | || | | | | | | |__  
  | | |  _  ||  __|  | |\/| | | | || | | | | | |  __| 
  | | | | | || |___  | |  | \ \_/ /\ \_/ /_| |_| |___ 
  \_/ \_| |_/\____/  \_|  |_/\___/  \___/ \___/\____/ 

______ _____  _    _ _   _  _     _____  ___ ______ ___________ 
|  _  \  _  || |  | | \ | || |   |  _  |/ _ \|  _  \  ___| ___ ?
| | | | | | || |  | |  \| || |   | | | / /_\ \ | | | |__ | |_/ /
| | | | | | || |/\| | . ` || |   | | | |  _  | | | |  __||    / 
| |/ /\ \_/ /\  /\  / |\  || |___\ \_/ / | | | |/ /| |___| |\ \ 
|___/  \___/  \/  \/\_| \_/\_____/\___/\_| |_/___/ \____/\_| \_|
""")
def chromedriver_availability():
    directory_for_linux = os.getcwd()
    # print(f"Your Current Directory Is: {directory_for_linux}")
    path_to_chromedriver= "/usr/bin"
    all_files = os.listdir(path_to_chromedriver)
    # print(all_files)
    if "chromedriver" in all_files:
        return True
    else:
        print("*************************************")
        print('fuck you go and install chromedriver')
        print("*************************************")
if chromedriver_availability() == True:
    print("*************************************")
    print('good to go')
    print("*************************************")
# GETTING THE WEBSITE
searchable = input('please enter the movie or webseries to search: ')
website_to_fire = "https://themoviesflix.in.net/"
driver = webdriver.Chrome()
driver.get(website_to_fire)
search_box = driver.find_element_by_xpath('//*[@id="s"]').send_keys(searchable)
search_button = driver.find_element_by_xpath('//*[@id="search-image"]/i').click()
current_page_url = driver.current_url
all_window_handles = driver.window_handles
driver.switch_to.window(all_window_handles[1])
driver.close()
# GETTING THE NAMES & LINKS OF MOVIES & WEB-SERIES
def names_and_links():
    ch = "category"
    website_to_scrape = current_page_url
    source = requests.get(website_to_scrape).text
    soup = BeautifulSoup(source, 'lxml')
    names = soup.find_all('article', class_="latestPost excerpt")
    # names of the movies/webseries that are available
    for row in names:  # Print all occurrences
        l = (row.get_text())
        print(l)
        print(" ")
    for data in soup.find_all('article', class_='latestPost excerpt'):
        for a in data.find_all('a'):  # for getting the links
            r = (a.get('href'))
            if ch in r:
                pass
            else:
                print(" ")
                print(r)

# GETTING EPISODES & SERVERS
names_and_links()
print(" ")
url_to_click = input("please enter the link: ")
print("")
requests.get(url_to_click)
# episodes
website_to_scrape1 = url_to_click
source2 = requests.get(website_to_scrape1).text
soup2 = BeautifulSoup(source2,'lxml')
for data in soup2.find_all('p',class_="has-text-align-center"):
    for link in data.find_all('a'):
        print(link.get('href'))
        print("")
        print(link.get_text())
for data2 in soup2.find_all('span',class_="mb-center maxbutton-3-center"):
    for link2 in data2.find_all('a'):
        print(link2.get('href'))
        print(" ")
        print(link2.get_text())
for data3 in soup2.find_all('span',class_="maxbutton-6-container mb-container"):
    for link3 in data3.find_all('a'):
        print(link3.get('href'))
        print(" ")
        print(link3.get_text())
for data4 in soup2.find_all('span',class_="maxbutton-13-container mb-container"):
    for link4 in data4.find_all('a'):
        print(link4.get('href'))
        print(" ")
        print(link4.get_text())
for data5 in soup2.find_all('div',class_="wp-block-button aligncenter"):
    for link5 in data5.find_all('a'):
        print(link5.get('href'))
        print(" ")
        print(link5.get_text())
print(" ")
next_link = input("ENTER THE NEXT LINK TO PROCEED WITH: ")
website_to_scrape2 = next_link
source3 = requests.get(website_to_scrape2).text
soup3 = BeautifulSoup(source3,'lxml')
for data2 in soup3.find_all('span',class_="maxbutton-7-container mb-container"):
    for link2 in data2.find_all('a'):
        print(link2.get_text())
        print(link2.get('href'))
        print(" ")
for data3 in soup3.find_all('span',class_="maxbutton-8-container mb-container"):
    for link3 in data3.find_all('a'):
        print(link3.get_text())
        print(link3.get('href'))
        print(" ")
for data4 in soup3.find_all('span',class_="maxbutton-9-container mb-container"):
    for link4 in data4.find_all('a'):
        print(link4.get_text())
        print(link4.get('href'))
        print(" ")
for data5 in soup3.find_all('span',class_="maxbutton-10-container mb-container"):
    for link5 in data5.find_all('a'):
        print(link5.get_text())
        print(link5.get('href'))
        print(" ")
for data6 in soup3.find_all('span',class_="maxbutton-11-container mb-container"):
    for link6 in data6.find_all('a'):
        print(link6.get_text())
        print(link6.get('href'))
        print(" ")

for data7 in soup3.find_all('span',class_="maxbutton-12-container mb-container"):
    for link7 in data7.find_all('a'):
        print(link7.get_text())
        print(link7.get('href'))
        print(" ")

for data8 in soup3.find_all('span',class_="maxbutton-13-container mb-container"):
    for link8 in data8.find_all('a'):
        print(link8.get_text())
        print(link8.get('href'))
        print(" ")

for data9 in soup3.find_all('span',class_="maxbutton-14-container mb-container"):
    for link9 in data9.find_all('a'):
        print(link9.get_text())
        print(link9.get('href'))
        print(" ")
# for data34 in soup3.find_all('span',class_="maxbutton-7-container mb-container"):
#     for link456 in data34.find_all('a'):
#         print(link456.get('href'))
#         print(" ")
#         print(link456.get_text())
for data25 in soup3.find_all('span',class_="maxbutton-2-container mb-container"):
    for link6871 in data25.find_all('a'):
        print(link6871.get('href'))
        print(" ")
        print(link6871.get_text())
for data39 in soup3.find_all('span',class_="maxbutton-35-container mb-container"):
    for link2069 in data39.find_all('a'):
        print(link2069.get('href'))
        print(" ")
        print(link2069.get_text())
next_next_link = input("PLEASE ENTER THE NEXT LINK AGAIN: ")
page = requests.get(next_next_link).text
soup = BeautifulSoup(page,'lxml')
onclick_link = soup.find('div',class_="col-md-12 text-center")
print(onclick_link)
