# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:09:12 2020

@author: MonOrdiPro
"""
import dash_core_components as dcc
import historical_scraper as hs
import dash_html_components as html
import colors as colors

data = hs.get_data()




def get_content(country):

    return html.Div([
        dcc.Graph(
         
          figure={
            'data': [
              {'x': data['Date'], 'y': data[data["Country"] == country]['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data['Date'], 'y': data[data["Country"] == country]['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
              {'x': data['Date'], 'y': data[data["Country"] == country]['New Cases'], 'type': 'bar', 'name': 'New Cases'},
              {'x': data['Date'], 'y': data[data["Country"] == country]['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
            ],

          }
    ),       
            
            ])
