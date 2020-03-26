import dash_core_components as dcc
import historical_scraper as hs
import dash_html_components as html

data = hs.get_data() # à remplacer par une requête en db pour plus de perfs une fois que la db sera créée

unique_country = data.Country.unique()

def get():
  countries = [{'label': country, 'value': country} for country in unique_country]
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
    

