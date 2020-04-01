# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:14:24 2020

@author: MonOrdiPro
"""
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import pandas as pd
import os
from chloro_map_tab4 import sum_journaliere_rea
from chloro_map_tab4 import sum_journaliere_deces
from chloro_map_tab4 import sum_journaliere_hospit
from plotly.subplots import make_subplots


colors = colors.get()


data_folder = './map/archive'
files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]
jours = {}
i=0
for elt in files :
    jours[i] = elt[-9:-4]
    i+=1
jours[len(jours)-1]
titre = 'France data per department\n( last update : 2020-{} )'.format(jours[len(jours)-1].replace('_','-')) 



list_percent_raise_rea = []

for i in range (len(sum_journaliere_rea)-1) :
    list_percent_raise_rea.append((sum_journaliere_rea[i+1]-sum_journaliere_rea[i]) * 100 / sum_journaliere_rea[i])           



# création du graph par somme journaliere :

fig = go.Figure()
fig = make_subplots(rows=1, cols=2)
fig.add_trace(
        go.Bar(
                x= [jour for jour in jours.values()],
                y= sum_journaliere_hospit
                ),
            row = 1,
            col = 1,
            
        )

fig.add_trace(
        go.Scatter(
               x= [jour for jour in jours.values()],
               y= sum_journaliere_deces
               ),
        row = 1,
        col = 2,

        )
fig.add_trace(
        go.Scatter(
               x= [jour for jour in jours.values()],
               y= sum_journaliere_rea
               ),
        row = 1,
        col = 2,

        )
fig.update_layout(
        title= {'text': "Plot Title"},
        paper_bgcolor= colors['background'],
        plot_bgcolor = colors['background'],
        )


fig.update_xaxes(color = 'grey', gridcolor='#303030')
fig.update_yaxes(color = 'grey',gridcolor='#303030')
                 

"""                 
fig.update_annotations(dict(
        xref='2000',
        yref='22_03',
        text = 'yo'
        
        ))
"""


def get_content():
  return html.Div([

    html.Div([
        html.H6(
            children=titre ,
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        html.Br(),
        html.Br(),
        dcc.RadioItems(
                        className='radio',
                        id='check_option',
                        style={
                                'height': '40px',
                                'align-items': 'center',
                                'background-color': '#2d2d2d',
                                'width': '57%',
                                'left': '23%',
                                'position': 'absolute',
                                'display': 'flex',
                                'justify-content' : 'space-evenly',
                                'color' : 'rgb(186, 137, 126)',
                                'border-radius': '14px',
                                'box-shadow': 'rgb(132, 107, 107) 0px 0px 10px',
                            },
                        options = [
                                {'label' : 'Mort', 'value' : 'mort'},
                                {'label' : 'hospitalisation' , 'value' : 'hospitalisation'},
                                {'label' : 'réanimation', 'value' : 'reanimation'}
                                ],
                        value = 'mort'),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(dcc.Slider(
        id='crossfilter-day-slider',
        
        min=0,
        max=len(files)-1,
        value=len(files)-1,
        marks=jours,
        step=None,
        updatemode='drag'
        ),style={'width' : '44%', 'position' :'relative', 'left' : '29%', 'margin-bottom':'30px'}),        
        


        

    ]),
    html.Div(id='french_map'),
    dcc.Graph(
        id='example-graph-2',
        figure=fig,
        
    )
    
    


  ])