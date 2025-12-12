import requests
from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
print(f"Page Title: {title}")
# --------------------------------------------------
url = "https://www.scrapethissite.com/pages/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print("Links found:")
for link in links:
    href = link.get('href')
    if href:
        print(href)
# --------------------------------------------------
url = "https://www.scrapethissite.com/pages/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all(['th', 'td'])
    data = []
    for cell in cells:
        data.append(cell.text.strip())
    if data:
        print(data)
# ------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("Python Web Scraping")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
print(driver.title)
driver.quit()
# ------------------------------------------------
from bs4 import BeautifulSoup
import csv
html = """
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Cherry</li>
</ul>
"""
soup = BeautifulSoup(html, 'html.parser')
fruits = [li.text for li in soup.find_all('li')]
with open('fruits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fruit']) 
    for fruit in fruits:
        writer.writerow([fruit])
print("Saved to fruits.csv")