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
from graph_tab3 import data

colors = colors.get()

df_evolution = data[(data['Total Deaths'] > 10)]
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
    list_percent_raise_rea.append(int((sum_journaliere_rea[i+1]-sum_journaliere_rea[i]) * 100 / sum_journaliere_rea[i]))         

list_percent_raise_deces = []

for i in range (len(sum_journaliere_deces)-1) :
    list_percent_raise_deces.append(int((sum_journaliere_deces[i+1]-sum_journaliere_deces[i]) * 100 / sum_journaliere_deces[i])) 

list_percent_raise_hospit = []

for i in range (len(sum_journaliere_hospit)-1) :
    list_percent_raise_hospit.append(int((sum_journaliere_hospit[i+1]-sum_journaliere_hospit[i]) * 100 / sum_journaliere_hospit[i])) 



# création du graph par somme journaliere :

fig = go.Figure()
fig = make_subplots(rows=1, cols=2, specs=[[{"secondary_y": "False"}, {"secondary_y": "True"}]])

fig.add_trace(
        go.Scatter(
                x= [jour for jour in jours.values()],
                y= sum_journaliere_hospit,
                name='number of hospitalisation',
                hoverinfo='y',
                line=dict(color='#4d4dff')
                ),
            row = 1,
            col = 1,
            secondary_y=False
        )
fig.add_trace(
        go.Scatter(
                x=[jour for jour in list(jours.values())[1:]],
                y = list_percent_raise_hospit,
                line=dict(color='#9999ff', width=1, dash='dash'),
                name='% hospitalisation evolution from day -1',
                hoverinfo='y',
                ),
         
        row=1,
        col=1,
        secondary_y=True
        )

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

fig.add_trace(
        go.Scatter(
               x= [jour for jour in jours.values()],
               y= sum_journaliere_rea,
               name='number of person in reanimation',
               hoverinfo='y',
               line=dict(color='#5bd75b')
               
               ),
        row = 1,
        col = 2,
        secondary_y=False
        )
fig.add_trace(
        go.Scatter(
                x=[jour for jour in list(jours.values())[1:]],
                y = list_percent_raise_rea,
                line=dict(color='#239023', width=1, dash='dash'),
                name='% reanimation evolution from day -1',
                hoverinfo='y',
                ),
        
        row=1,
        col=2,
        secondary_y=True
        )
        
        
        

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

                 
fig.update_layout(
        title= {'text': "Plot Title"},
        paper_bgcolor= colors['background'],
        plot_bgcolor = colors['background'],
        xaxis=dict(showgrid=True, zeroline=True)
        )
                
fig.update_yaxes(color = 'grey',gridcolor='#303030')
   

df_evolution
jours_china_deaths = 50


fig2 = go.Figure()

fig2.add_trace(
        go.Scatter(
                x= [ x for x in range (1, jours_china_deaths)],
                y= df_evolution[df_evolution['Country'] == 'China']['Total Deaths'],
                name='China',
                hoverinfo='name + y',
                line=dict(color='#FFA500')
                ),

        )

fig2.add_trace(
        go.Scatter(
                x= [ x for x in range (1, jours_china_deaths)],
                y= df_evolution[df_evolution['Country'] == 'France']['Total Deaths'],
                name='France',
                hoverinfo='name + y',
                line=dict(color='#DC143C')
                ),
        )

fig2.add_trace(
        go.Scatter(
                x= [ x for x in range (1, jours_china_deaths)],
                y= df_evolution[df_evolution['Country'] == 'Spain']['Total Deaths'],
                name='Spain',
                hoverinfo='name + y',
                line=dict(color='#6495ED')
                ),

        )

                
fig2.add_trace(
        go.Scatter(
                x= [ x for x in range (1, jours_china_deaths)],
                y= df_evolution[df_evolution['Country'] == 'Italy']['Total Deaths'],
                name='Italy',
                hoverinfo='name + y',
                line=dict(color='#9932CC')
                ),


        )

fig2.add_trace(
        go.Scatter(
                x= [ x for x in range (1, jours_china_deaths)],
                y= df_evolution[df_evolution['Country'] == 'United States']['Total Deaths'],
                name='USA',
                hoverinfo='name + y',
                line=dict(color='#008000')
                ),


        )
               
                


fig2.update_yaxes(title_text="<b>percentage change compared<br> to the previous day</b>", 

                 showgrid=False,
                 color = 'grey',
                 gridcolor='#303030')

fig2.update_xaxes(color = 'grey', 
                 gridcolor='#303030', 
                 linecolor='#111111', 

                 showgrid=True,
                 title_text ="<b>Day<b>")

                 
fig2.update_layout(
        title= {'text': "Plot Title"},
        paper_bgcolor= colors['background'],
        plot_bgcolor = colors['background'],
        xaxis=dict(showgrid=True, zeroline=True)
        )
                


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

        ),style={'width' : '44%', 'position' :'relative', 'left' : '29%', 'margin-bottom':'30px'}),        
        


        

    ]),
    html.Div(id='french_map'),
    dcc.Graph(
        id='example-graph-2',
        figure=fig,
        
    ),
    
    html.Div([
    dcc.Graph(
        id='graph_3',
        figure=fig2,
        
    )],className = 'six columns',id='international_comparative'),    


  ])