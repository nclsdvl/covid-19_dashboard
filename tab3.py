# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import countries_dropdown as countries_dropdown

colors = colors.get()

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
    ])
  ])