# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import countries_dropdown as countries_dropdown
import scraper as scrap
import historical_scraper as hs

country = 'France'
 
colors = colors.get()
data = scrap.get_data()

print(data[data.index == country]['Total Cases'])

def get_content():
  return html.Div([
    html.H6(
        children='Select your country',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
      html.Div([
        countries_dropdown.get()
      ])
    ]),
    
    html.Div(id='country-data'
 
            
        ),

  ], 
    
    )
