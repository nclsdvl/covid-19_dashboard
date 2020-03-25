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
    
    html.Div([
       dcc.Graph(
         id='country-data',
          figure={
            'data': [
              {'x': 'Total Cases', 'y': data[data.index == country]['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': 'Total Deaths', 'y': data[data.index == country]['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
              {'x': 'New Cases', 'y': data[data.index == country]['New Cases'], 'type': 'bar', 'name': 'New Cases'},
              {'x': 'New Deaths', 'y': data[data.index == country]['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
            ],
            'layout': {
              'title': "Evolution of Covid-19 in the World since 31/12/2019",
              'plot_bgcolor': colors['background'],
              'bargap': '2',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
    ), 
            
        ]),
    html.Div(id='dd-output-container')
  ], 
    
    )
