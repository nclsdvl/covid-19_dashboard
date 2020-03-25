# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:26:43 2020

@author: MonOrdiPro
"""
import os
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html

"""
A -> -15 ans
B -> 15-44
C -> 45-64
D -> 65-74
E -> +75
"""

data1 = pd.read_csv('./donnée_covid_fr/data_clean_22_03.csv')
data1.dtypes
test = data1[data1['sursaud_cl_age_corona'] == 'A']


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Covid-19 Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    # Total Cases europe de l'est
    html.Div([
        dcc.Graph(
            id='total-cases-europe-est',
            figure={
                'data': [
                    {'x': data1.index, 'y': data1[data1['sursaud_cl_age_corona'] == 'A'], 'type': 'bar', 'name': 'Total Cases'},
                    {'x': data1.index, 'y': data1[data1['sursaud_cl_age_corona'] == 'B'], 'type': 'bar', 'name': 'Total Recovered'},
                    {'x': data1.index, 'y': data1[data1['sursaud_cl_age_corona'] == 'C'], 'type': 'bar', 'name': 'Total Deaths'}
                ],
                'layout': {
                    'title': "Total Cases from the ten's most affected country in east europe",
                    'plot_bgcolor': colors['background'],
                    'bargap': '2',
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    
    
            
    ], className = 'row'),
    

    
   
    




])

if __name__ == '__main__':
    app.run_server(debug=False)