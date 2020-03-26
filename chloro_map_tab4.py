# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:33:03 2020

@author: MonOrdiPro
"""
import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import json
import pandas as pd
import plotly.express as px
import os



dir_path = os.path.dirname(os.path.realpath(__file__))
geojson_file = os.path.join(dir_path, 'map/departements.geojson')
csv_file = os.path.join(dir_path, 'map/data_clean_23_03.csv')

colors = colors.get()
with open(geojson_file, 'r', encoding='utf-8') as f:
    t = f.read()
    locations = json.loads(t)
    

# fig.show()  # J'ai commenté le show car il ouvre un nouvel onglet systématiquement ;)




def get_content(case) :
    col_name = ''
    print(case)
    if case == 'mort' :
        col_name = 'Nombre cumulé total décédées 2020-03-23'
    elif case == 'hospitalisation' :
        col_name = 'Nombre total actuellement hospitalisées 2020-03-23'
    elif case == 'reanimation' :
        col_name = 'Nombre total actuellement en réanimation ou soins intensifs 2020-03-23'
    
    df = pd.read_csv(csv_file, encoding='utf-8') 
    df = df.rename(columns={'Code': 'code'})
    
    
    
    fig = px.choropleth(df, geojson=locations, color=col_name,
                        locations="Libellé", featureidkey="properties.nom", template="plotly_dark",
                        projection="mercator"
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(paper_bgcolor='#111')  
    
    
    
    
    
    
    return  html.Div([
                
                dcc.Graph(
                    className='eight columns',
                    style={
                            'backgroundColor':'#111'
                            },
                    id='French_chloro_map',
                    figure = fig,
                )   
                    
            ], className='row',
                style={
                        'vertical-align': 'middle'
                })