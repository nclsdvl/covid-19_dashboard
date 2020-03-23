# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import scraper as scrap
import tab1 as tab1
import tab2 as tab2
import colors as colors

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = colors.get()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Covid-19 Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Today\'s data', value='tab-1'),
        dcc.Tab(label='Historical data', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
  if tab == 'tab-1':
    return tab1.get_content()
  elif tab == 'tab-2':
    return tab2.get_content()

if __name__ == '__main__':
    app.run_server(debug=True)