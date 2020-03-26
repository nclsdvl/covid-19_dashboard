# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 06:32:56 2020

@author: MonOrdiPro
"""
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import colors as colors

colors = colors.get()

def get (nb_homme, nb_femme) :
   total = nb_homme + nb_femme 
   data = [
    {
        'values': [nb_homme, nb_femme],
        'type': 'pie',
        'labels' : ['homme', 'femme'],
        
        },
    ]
       
    
    
   return html.Div([
            dcc.Graph(
            id='pie_gender',
            figure={
                    'data':data,
                    'layout': {
                      'title': "Total rate by gender <br>( total : "+str(total)+" )",
                      'paper_bgcolor': colors['background'],
                      'font': {
                          'color': colors['text']
                      }
                    },    
                })
    ],className='four columns')