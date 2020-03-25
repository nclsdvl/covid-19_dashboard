import dash_core_components as dcc
import scraper as scrap
import dash_html_components as html

data = scrap.get_data() # à remplacer par une requête en db pour plus de perfs une fois que la db sera créée

def get():
  countries = [{'label': country, 'value': country} for country in data.index]
  return html.Div([
        dcc.Dropdown(
        id='countries-dropdown',

        options=countries,
        value='France'
        )
    ], style = {
                'margin-left': '40%',
                'width' : '20%',
                'margin-right': '35%'},)
    

