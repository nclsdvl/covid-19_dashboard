# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import scraper as scrap
import colors as colors

colors = colors.get()

# getting data from scraping module
data = scrap.get_data()
data['percentage D/C'] = data['Total Deaths']/data['Total Cases']*100

data_europe_est = data[data['Continent'] == "Europe de l'est"][:10]
data_europe_ouest = data[data['Continent'] == "Europe de l'ouest"][:10]
data_amerique = data[data['Continent'] == 'Amerique'][:10]
data_oceanie = data[data['Continent'] == 'Oceanie']
data_afrique = data[data['Continent'] == 'Afrique'][:10]
data_asie = data[data['Continent'] == 'Asie'][:10]
data_asie_occ = data[data['Continent'] == 'Asie occidentale'][:10]
data_autre = data[data['Continent'] == 'Autres']

def get_content():
  return html.Div([
    html.Div([
      html.Div([
        # Total Cases europe de l'est
        dcc.Graph(
          id='total-cases-europe-est',
          figure={
            'data': [
              {'x': data_europe_est.index, 'y': data_europe_est['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_europe_est.index, 'y': data_europe_est['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_europe_est.index, 'y': data_europe_est['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in Eastern Europe",
              'plot_bgcolor': colors['background'],
              'bargap': '2',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className='six columns'),
      html.Div([
        # Total Cases europe de l'ouest
        dcc.Graph(
          id='total-cases-europe-ouest',
          figure={
            'data': [
              {'x': data_europe_ouest.index, 'y': data_europe_ouest['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_europe_ouest.index, 'y': data_europe_ouest['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_europe_ouest.index, 'y': data_europe_ouest['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in Western Europe",
              'plot_bgcolor': colors['background'],
              'width': '50',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className = 'six columns'), 
    ], className = 'row'),
    html.Div([
      html.Div([
        # Total Cases Afrique
        dcc.Graph(
          id='total-cases-afrique',
          figure={
            'data': [
              {'x': data_afrique.index, 'y': data_afrique['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_afrique.index, 'y': data_afrique['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_afrique.index, 'y': data_afrique['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in Africa",
              'plot_bgcolor': colors['background'],
              'bargap': '2',
              'paper_bgcolor': colors['background'],
              'font': {
                'color': colors['text']
              }
            }
          }
        )
      ], className='six columns'),
      html.Div([
        # Total Cases Amérique
        dcc.Graph(
          id='total-cases-amerique',
          figure={
            'data': [
              {'x': data_amerique.index, 'y': data_amerique['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_amerique.index, 'y': data_amerique['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_amerique.index, 'y': data_amerique['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in America",
              'plot_bgcolor': colors['background'],
              'width': '50',
              'paper_bgcolor': colors['background'],
              'font': {
                'color': colors['text']
              }
            }
          }
        )
      ], className = 'six columns'),    
    ], className = 'row'), 
    html.Div([
      html.Div([
        # Total Cases Asie de l'est
        dcc.Graph(
          id='total-cases-east-asia',
          figure={
            'data': [
              {'x': data_asie.index, 'y': data_asie['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_asie.index, 'y': data_asie['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_asie.index, 'y': data_asie['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in Eastern Asia",
              'plot_bgcolor': colors['background'],
              'bargap': '2',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className='six columns'),
      html.Div([
        # Total Cases Asie de l'ouest
        dcc.Graph(
          id='total-cases-west-asia',
          figure={
            'data': [
              {'x': data_asie_occ.index, 'y': data_asie_occ['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_asie_occ.index, 'y': data_asie_occ['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_asie_occ.index, 'y': data_asie_occ['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from the ten most affected countries in Western Asia",
              'plot_bgcolor': colors['background'],
              'width': '50',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className = 'six columns'),     
    ], className = 'row'),    
    html.Div([
      html.Div([
        dcc.Graph(
          id='total-cases-oceanie',
          figure={
            'data': [
              {'x': data_oceanie.index, 'y': data_oceanie['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_oceanie.index, 'y': data_oceanie['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_oceanie.index, 'y': data_oceanie['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from Oceania",
              'plot_bgcolor': colors['background'],
              'bargap': '2',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className='six columns'),
      html.Div([
        # Total Cases Autres
        dcc.Graph(
          id='total-cases-other',
          figure={
            'data': [
              {'x': data_autre.index, 'y': data_autre['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': data_autre.index, 'y': data_autre['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
              {'x': data_autre.index, 'y': data_autre['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
              'title': "Total Cases from Other",
              'plot_bgcolor': colors['background'],
              'width': '50',
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )
      ], className = 'six columns'),     
    ], className = 'row'),  
    html.Div([
      html.Div([ 
        # Death ratio per Country Graph
        dcc.Graph(
          id='ratio-per-country-graph',
          figure={
            'data': [
              {'x': data.index, 'y': data['percentage D/C'], 'type': 'bar'}
            ],
            'layout': {
              'title': 'Deaths/Cases Percentage',
              'plot_bgcolor': colors['background'],
              'paper_bgcolor': colors['background'],
              'font': {
                  'color': colors['text']
              }
            }
          }
        )  
      ], className = 'twelwe columns'),
    ], className = 'row')
  ])     