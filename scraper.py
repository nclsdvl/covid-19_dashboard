# -*- coding: utf-8 -*-
import requests
import bs4 as BeautifulSoup
import pandas as pd 
import numpy as np
from atr_continent import attribution_continent

def pretty(string):
  return string.replace(',','').strip()

def get_data():
  url = 'https://www.worldometers.info/coronavirus/'
  html_table_id = "main_table_countries_today"
  html = requests.get(url).text
  soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
  table = soup.find(id=html_table_id)
  tbody = table.findChildren("tbody" , recursive=False)[0]
  rows = tbody.find_all('tr')

  countries = []
  indexes = []
  for row in rows:
    cols = row.find_all('td')
    indexes.append(cols[0].text)
    country = [
      pretty(cols[1].text),
      pretty(cols[2].text),
      pretty(cols[3].text),
      pretty(cols[4].text),
      pretty(cols[5].text),
      pretty(cols[6].text),
      pretty(cols[7].text)
    ]
    countries.append(country)

  columns = ['Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious, Critical']

  data = pd.DataFrame(countries, index=indexes, columns = columns, dtype="i") 
  data = data.replace(r'^\s*$', np.nan, regex=True).fillna(0)
  data = data.astype('int')
  attribution_continent(data)
  return data