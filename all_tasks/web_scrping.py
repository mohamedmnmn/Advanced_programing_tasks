import requests
from bs4 import BeautifulSoup

def par(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    par = soup.find_all("p")
    for p in par:
        print(p.text.strip())
def herf(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    print("Links found:")
    for link in links:
        href = link.get('href')
        if href:
            print(href)
def table(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table')

    if table is None:
        print("No table found on this page.")
        return

    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        data = [cell.text.strip() for cell in cells]
        if data:
            print(data)
url = input('Enter url')

print('what do you want to do?')
print('1.Get paragraph')
print('2.Get links')
print('3.Get table')
x= int(input())
if x==1:
    par(url)
elif x==2:
    herf(url)
elif x==3:
    table(url)
else:
    print('entar a valid number')
