# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:09:12 2020

@author: MonOrdiPro
"""
import dash_core_components as dcc
import historical_scraper as hs
import dash_html_components as html
import colors as colors
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


colors = colors.get()

country = 'France'


data = hs.get_data()
data[['New Cases', 'New Deaths', 'Total Deaths', 'Total Cases']] = data[['New Cases', 'New Deaths', 'Total Deaths', 'Total Cases']].apply(pd.to_numeric)
df_evolution = data[(data.Country == country) & (data['Total Deaths'] > 10)]

def get_content(country):
    
    
    country_data = data[data['Country'] == country]
    

    """
    list_percent_raise_cases = []
    for i in range (1, len(df_evolution)) :         
        list_percent_raise_cases.append(int((int(df_evolution[i:i+1]['Total Cases'])-int(df_evolution[i-1:i]['Total Cases'])) * 100 / int(df_evolution[i-1:i]['Total Cases'])))         

    
    
    
    
    
    fig = go.Figure()
    fig = make_subplots(rows=1, cols=2, specs=[[{"secondary_y": "False"}, {"secondary_y": "True"}]])
    
    fig.add_trace(
        go.Scatter(
                x= df_evolution['Date'],
                y= df_evolution['Total Cases'],
                name='number of cases',
                hoverinfo='y',
                line=dict(color='#4d4dff')
                ),
            row = 1,
            col = 1,
            secondary_y=False
        )
    fig.add_trace(
        go.Scatter(
                x= df_evolution['Date'],
                y = list_percent_raise_cases,
                line=dict(color='#9999ff', width=1, dash='dash'),
                name='% hospitalisation evolution from day -1',
                hoverinfo='y',
                ),
         
        row=1,
        col=1,
        secondary_y=True
        )
    fig.update_layout(
            title= {'text': "Plot Title"},
            paper_bgcolor= colors['background'],
            plot_bgcolor = colors['background'],
            xaxis=dict(showgrid=True, zeroline=True)
            )
                    
    fig.update_yaxes(color = 'grey',gridcolor='#303030')  
    fig.update_yaxes(title_text="<b>percentage change compared<br> to the previous day</b>", 
                 secondary_y=True, 
                 row=1, col=1, 
                 showgrid=False,
                 color = 'grey',
                 gridcolor='#303030')
    fig.update_yaxes(title_text="<b>percentage change compared<br> to the previous day</b>", 
                     secondary_y=True,
                     row=1, col=2, 
                     range=[0, 70],
                     showgrid=False,
                     color = 'grey',
                     gridcolor='#303030'
                     )
    
    fig.update_xaxes(color = 'grey', 
                     gridcolor='#303030', 
                     linecolor='#111111', 
                     row=1, col=2,
                     showgrid=True,
                     title_text ="<b>Day<b>")
    fig.update_xaxes(color = 'grey', 
                     gridcolor='#303030', 
                     linecolor='#111111', 
                     row=1, col=1, 
                     title_text ="<b>Day<b>",
                     showgrid=True,)                

                 

                    
        fig.add_trace(
            go.Scatter(
                   x= [jour for jour in jours.values()],
                   y= sum_journaliere_deces,
                   name='number of dead',
                   hoverinfo='y',
                   line=dict(color='#ff1a1a')
                   ),
            row = 1,
            col = 2,
            secondary_y=False
            )              
    fig.add_trace(
            go.Scatter(
                    x=[jour for jour in list(jours.values())[1:]],
                    y = list_percent_raise_deces,
                    line=dict(color='#ff8080', width=1, dash='dash'),
                    name='% dead evolution from day -1',
                    hoverinfo='y',
                    ),
             
            row=1,
            col=2,
            secondary_y=True
            )
    """    
 
    
    
    return html.Div([
        dcc.Graph(
          figure={
            'data': [
              {'x': country_data['Date'], 'y': country_data['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
              {'x': country_data['Date'], 'y': country_data['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'},
              {'x': country_data['Date'], 'y': country_data['New Cases'], 'type': 'bar', 'name': 'New Cases'},
              {'x': country_data['Date'], 'y': country_data['New Deaths'], 'type': 'bar', 'name': 'New Deaths'}
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
    
        """
        dcc.Graph(
        id='example-graph-3',
        figure=fig,
        
    )
    """
    
    
    ])
