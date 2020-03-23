import dash_core_components as dcc
import scraper as scrap

data = scrap.get_data() # à remplacer par une requête en db pour plus de perfs une fois que la db sera créée

def get():
  countries = [{'label': country, 'value': country} for country in data.index]
  return dcc.Dropdown(
    id='countries-dropdown',
    options=countries,
    value='France'
  )