# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import historical_scraper as hs

colors = colors.get()
data = hs.get_data() 

world_data = data[data['Country'] == 'World']

def get_content():
  return html.Div([
    dcc.Graph(
      id='historical-world-data',
      figure={
        'data': [
          {'x': world_data['Date'], 'y': world_data['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
          {'x': world_data['Date'], 'y': world_data['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
          {'x': world_data['Date'], 'y': world_data['New Cases'], 'type': 'bar', 'name': 'New Cases'},
          {'x': world_data['Date'], 'y': world_data['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
        ],
        'layout': {
          'title': "Evolution of Covid-19 since 31/12/2019",
          'plot_bgcolor': colors['background'],
          'bargap': '2',
          'paper_bgcolor': colors['background'],
          'font': {
              'color': colors['text']
          }
        }
      }
    )
  ])