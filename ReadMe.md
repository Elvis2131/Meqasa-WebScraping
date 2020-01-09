#  Web Scraping

The aim of this project was to scrape housing information from [MeQasa](https://meqasa.com/), clean the data(monitor errors, standardize the process, validating accuracy, scrubing duplicate data and analyzing) and save the dataframe in a CSV format.

## DataFrame structure
* property
* beds
* showers
* garages
* area
* description
* price
* curreny (GHS or $)
* url 
* address
* time_posted

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to run the script.

* Python: for the data manipulation.
* Gitbash: For pushing the files your repo.
* An IDE(VScode or Jupyter Notebook): To run and edit the codes 

### Installing

A step by step series of examples that tell you how to get a development env running

* Install python on your system(macOS, windows or Linux)
* Clone repo.
* Install the required dependencies.
```
pip install requests beautifulsoup4 lxml
```

