#importing required libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

def main():
    #Declaring variables to hold the going to be scraped data.
    garage = []
    address = []
    broker = []
    area = []
    description = []
    broker = []
    posting = []
    property_title = []
    property_url = []
    bedCount = []
    priceCount = []
    showerCount = []

    #Scraping the needed data from meqasa from page 1 to 10(houses for rent page into the declared list variables)
    for x in range(1,11):
        results = requests.get('https://meqasa.com/houses-for-rent-in-ghana?w='+str(x))
        soup = BeautifulSoup(results.content, 'html.parser')
        container = soup.find('div', class_='filtRpg')

        for info in container.find_all('div', class_='mqs-prop-dt-wrapper'):
        property_title.append(info.find('h2').text)#scraping the property's title
        bedCount.append(info.find('li', class_='bed').text)#scraping the property's number of bed
        property_url.append('https://meqasa.com'+ info.find('a', href=True)['href'])#scraping the property's url
        #scraping the property's cost and cleaning the data
        priceCount.append(info.find('p', class_='h3').text.replace('\n', '').replace('$', ' $').replace('GH₵', ' GH₵').replace(' / month', '').replace(' / day', '').replace('Price ','').replace('Price:',''))
        showerCount.append(info.find('li', class_='shower').get_text())#scraping the property's number of bathroom
        
        #scraping the property's number of garage and size of the property
        if info.find('li',class_='garage') is None:
            garage.append('n.a')
        else:
            garage.append(info.find('li',class_='garage').text)
        
        if info.find('li',class_='area') is None:
            area.append('n.a')
        else:
            area.append(info.find('li',class_='area').text)

        #Using the scraped url to get into each property to scrape information such as
        #the property's location, date posted and the broker.
        more_info = requests.get(property_url[len(property_url) -1])
        info_soup = BeautifulSoup(more_info.content, 'html.parser')
        results = info_soup.find('div', class_='description').text.replace('\n','')
        description.append(results)

        for cells in info_soup.find_all('table'):
            cell = cells.find_all('td')
            address.append(cell[-2].get_text())
            
        for date in info_soup.find_all('p', class_='listed-by-text'):
            answer = date.get_text().replace('Updated on ','').replace(' by:','')
            posting.append(answer)

        for agent in info_soup.find_all('h2', class_='agent-name'):
            broker.append(agent.get_text().replace('\n',''))

        #Checking to see if the scraped data are of the same length as pandas requires
        print(len(property_title))
        print(len(bedCount))
        print(len(property_url))
        print(len(priceCount))
        print(len(showerCount))
        print(len(address))
        print(len(posting))
        print(len(garage))
        print(len(area))
        print(len(property_url))

        #putting the scraped data into a pandas dataframe.
            df = pd.DataFrame({
        'Title': property_title,
        'No. of bedroom': bedCount,
        'No. of bathroom': showerCount,
        'Garage size': garage,
        'Area': area,
        'Address': address,
        'Price': priceCount,
        'Date Posted': posting,
        'URL': property_url})

if __name__ == '__main__':
    main()