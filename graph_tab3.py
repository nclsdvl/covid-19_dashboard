# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:09:12 2020

@author: MonOrdiPro
"""
import dash_core_components as dcc
import historical_scraper as hs
import dash_html_components as html
import colors as colors

def get_content(country):
    data = hs.get_data()
    country_data = data[data['Country'] == country]
    return html.Div([
        dcc.Graph(
          figure={
            'data': [
              {'x': country_data['Date'], 'y': country_data['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': country_data['Date'], 'y': country_data['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
              {'x': country_data['Date'], 'y': country_data['New Cases'], 'type': 'bar', 'name': 'New Cases'},
              {'x': country_data['Date'], 'y': country_data['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
            ]
          }
        )
    ])
