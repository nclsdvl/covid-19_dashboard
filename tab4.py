# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:14:24 2020

@author: MonOrdiPro
"""

import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import json
import pandas as pd
import plotly.express as px



colors = colors.get()
with open('./map/departements.geojson', 'r', encoding='utf-8') as f:
    t = f.read()
    locations = json.loads(t)
    
df = pd.read_csv('./map/data_clean_23_03.csv', encoding='utf-8') 
df = df.rename(columns={'Code': 'code'})



fig = px.choropleth(df, geojson=locations, color="Nombre cumulé total décédées 2020-03-23",
                    locations="Libellé", featureidkey="properties.nom", template="plotly_dark",
                    projection="mercator"
    )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(paper_bgcolor='#111')
fig.show()



def get_content():
  return html.Div([

    html.Div([
        html.H6(
            children='French data on : {}'.format(df.columns[2][-10:]),
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        html.Br(),
        html.Br(),
        html.Div([
            dcc.Checklist(
                    className='one columns',
                    id='check_option',
                    style={
                            'vertical-align': 'middle',
                            'display': 'inline-flex',
                            'text-align': 'center',
                            'left': '43%',
                            'position': 'relative',
                        },
                    options = [
                            {'label' : 'Mort', 'value' : 'mort'},
                            {'label' : 'hospitalisation' , 'value' : 'hospitalisation'},
                            {'label' : 'réanimation', 'value' : 'reanimation'}
                            ]),
            dcc.Graph(
                className='eleven columns',
                style={
                        'backgroundColor':'#111'
                        },
                id='French_map',
                figure = fig,
            )   
                
        ], className='row',
            style={
                    'vertical-align': 'middle'
            }),

        

    ]),
    

  ], 
    
    )