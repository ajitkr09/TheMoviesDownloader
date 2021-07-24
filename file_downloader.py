from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pyfiglet import Figlet
from termcolor import colored

# PRINT
f = Figlet(font='doom')
print(colored(f.renderText('THE MOVIE DOWNLOADER') ,'red',))
# GETTING THE WEBSITE
searchable = input('please enter the movie or webseries to search: ')
website_to_fire = "https://themoviesflix.io/"
driver = webdriver.Chrome()
driver.get(website_to_fire)
search_box = driver.find_element_by_xpath('//*[@id="s"]').send_keys(searchable)
search_button = driver.find_element_by_xpath('//*[@id="search-image"]/i').click()
current_page_url = driver.current_url
all_window_handles = driver.window_handles
driver.switch_to.window(all_window_handles[1])
driver.close()
# GETTINF THE NAMES & LINKS OF WEBSERIES & WEB-SERIES
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
        print("")
    for data in soup.find_all('article', class_='latestPost excerpt'):
        for a in data.find_all('a'):  # for getting the links
            r = (a.get('href'))
            if ch in r:
                pass
            else:
                print(r)
                print()

# GETTING EPISODES & SERVERS
names_and_links()
url_to_click = input("please enter the link: ")
requests.get(url_to_click)
# episodes
website_to_scrape2 = url_to_click
source2 = requests.get(website_to_scrape2).text
soup2 = BeautifulSoup(source2,'lxml')
for data in soup2.find_all('p',class_="has-text-align-center"):
    for link in data.find_all('a'):
        print(link.get('href'))
        print(link.get_text())
for data2 in soup2.find_all('span',class_="maxbutton-3-container mb-container"):
    for link2 in data2.find_all('a'):
        print(link2.get('herf'))





