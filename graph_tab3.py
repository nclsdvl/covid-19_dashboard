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
    france_data = data[data['Country'] == 'France']
    return html.Div([
        dcc.Graph(
          figure={
            'data': [
              {'x': france_data['Date'], 'y': france_data['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': france_data['Date'], 'y': france_data['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
              {'x': france_data['Date'], 'y': france_data['New Cases'], 'type': 'bar', 'name': 'New Cases'},
              {'x': france_data['Date'], 'y': france_data['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
            ]
          }
        )
    ])
