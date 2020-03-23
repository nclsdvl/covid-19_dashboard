# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import scraper as scrap




# getting data from scraping module
data = scrap.get_data()
data['percentage D/C'] = data['Total Deaths']/data['Total Cases']*100



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Covid-19 Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    # Total Cases per Country Graph
    dcc.Graph(
        id='total-cases-per-country-graph',
        figure={
            'data': [
                {'x': data.index, 'y': data['Total Cases'], 'type': 'bar', 'name': 'Total Cases'},
                {'x': data.index, 'y': data['Total Recovered'], 'type': 'bar', 'name': 'Total Recovered'},
                {'x': data.index, 'y': data['Total Deaths'], 'type': 'bar', 'name': 'Total Deaths'}
            ],
            'layout': {
                'title': 'Total Cases per Country',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    # Death ratio per Country Graph
    dcc.Graph(
        id='ratio-per-country-graph',
        figure={
            'data': [
                {'x': data.index, 'y': data['percentage D/C'], 'type': 'bar'}
            ],
            'layout': {
                'title': 'Total Deaths/Total Cases Percentage',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )



])

if __name__ == '__main__':
    app.run_server(debug=True)