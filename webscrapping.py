import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

import boto3

def main():

results = ''
url = ''
soup = ''

url = "https://meqasa.com/properties-for-sale-in-ghana"
results = requests.get(url)
soup = BeautifulSoup(results.content, 'lxml')
    
url = "https://meqasa.com/properties-for-sale-in-ghana"
x = 1
titles = []
prices = []
descriptions =[]
beds =[]
bathrooms =[]
garages = []
spaces = []
results = requests.get(url)
soup = BeautifulSoup(results.content, 'lxml')
    
while x != 50:
    listing = soup.findAll('div', {'class':'row mqs-featured-prop-inner-wrap clickable'})
    data=[]
    x= x+1

    garage = soup.find('li',{'class':'garage'}).text
    bed = soup.find('li',{'class':'bed'}).text
    shower = soup.find('li',{'class':'shower'}).text
    area = soup.find('li',{'class':'area'}).text

    for tag in listing[x].find_all(['p','h2']):
        answer =tag.text.replace('\n','')
        data.append(answer)

    titles.append(data[0])

    if (data[1].replace('Price','').strip('').startswith('G')):
        prices.append('Ghana Cedis')
    else:
        prices.append('Dollars')


    descriptions.append(data[2])

    beds.append(bed)
    bathrooms.append(shower)
    garages.append(garage)
    spaces.append(area)

df_info = pd.DataFrame({
            'title': titles,
            'Price': prices,
            'description': descriptions,
            'Beds' : beds,
            'bathrooms': bathrooms,
            'garages': garages,
            'spaces':spaces
            })
    

   

if __name__ == '__main__':
        main()
        
