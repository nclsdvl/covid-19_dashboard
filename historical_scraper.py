import csv
import requests
import pandas as pd
import sys

CSV_URL = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'

def get_data():
  with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    csv_data = csv.reader(decoded_content.splitlines(), delimiter=',')
    rows = list(csv_data)[1:]
    columns = ['Date', 'Country', 'New Cases', 'New Deaths', 'Total Cases','Total Deaths']
    return pd.DataFrame(rows, columns = columns) 

