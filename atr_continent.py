# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 04:26:34 2020

@author: MonOrdiPro
"""

import pandas as pd 



europe_ouest = ['Italy', 'Spain', 'Germany', 'France','Switzerland','UK','Netherlands','Austria',
         'Belgium', 'Norway', 'Sweden', 'Portugal','Denmark', 'Turkey', 'Ireland',
         'Luxembourg', 'Poland', 'Finland', 'Greece', 'Iceland', 'Romania',
         'San Marino', 'Lithuania', 'Hungary','Faeroe Islands', 'Andorra', 'Malta', 'Ukraine', 
         'Liechtenstein', 'Channel Islands', 'Monaco', 'Gibraltar', 'Isle of Man', 'Vatican City']

europe_est = ['Czechia','Slovenia', 'Russia', 'Estonia','Croatia', 'Serbia','Bulgaria', 'Slovakia',
              'Bosnia and Herzegovina', 'North Macedonia','Armenia', 'Cyprus', 'Moldova', 'Albania',
              'Belarus', 'Georgia', 'Armenia','Montenegro',]

afrique = ['Egypt', 'South Africa', 'Algeria','Morocco', 'Burkina Faso', 'Tunisia', 'Réunion', 'Cameroon',
           'DRC', 'Nigeria', 'Mauritius', 'Ghana', 'Rwanda', 'Togo', 'Kenya','Ivory Coast', 'Tanzania', 'Ethiopia',
           'Mayotte', 'Seychelles', 'Equatorial Guinea', 'Gabon', 'Suriname', 'Eswatini', 'Cabo Verde', 'Congo', 
           'Liberia', 'Madagascar', 'Namibia', 'Zambia', 'Zimbabwe', 'Sudan', 'Angola', 'Benin', 'Guinea',
           'Mauritania', 'Niger', 'Chad', 'Djibouti','Eritrea','Gambia','Mozambique', 'Somalia','Uganda']

amerique = ['USA', 'Brazil', 'Canada', 'Ecuador', 'Chile','Peru', 'Panama', 'Argentina', 'Mexico','Colombia',
            'Dominican Republic', 'Uruguay', 'Costa Rica', 'Venezuela', 'Senegal', 'Guadeloupe','Trinidad and Tobago',
            'Martinique', 'Cuba', 'Honduras', 'Bolivia', 'Puerto Rico','Paraguay', 'Guatemala', 'Guyana', 
            'Jamaica', 'French Guiana','Barbados','Aruba', 'Bermuda', 'U.S. Virgin Islands', 'Saint Martin',
            'Bahamas', 'Greenland', 'Cayman Islands', 'Curaçao', 'El Salvador', 'St. Barth','Haiti',
            'Nicaragua', 'Saint Lucia', 'Antigua and Barbuda', 'Dominica', 'Grenada','Montserrat',
            'St. Vincent Grenadines', 'Sint Maarten']

asie = ['China',  'S. Korea', 'Malaysia', 'Japan',  'Pakistan', 'Thailand',
        'Indonesia', 'Singapore', 'India', 'Philippines', 'Russia', 'Taiwan', 'Afghanistan',
        'Hong Kong',  'Vietnam', 'Cambodia', 'Sri Lanka', 'Azerbaijan', 'Kazakhstan', 'Uzbekistan',
        'Bangladesh', 'Macao','Kyrgyzstan', 'Maldives', 'Mongolia', 'Bhutan', 'Nepal', 'Timor-Leste']

asie_occidentale = ['Iran','Turkey','Israel','Saudi Arabia', 'Qatar', 'Bahrain','Lebanon', 'Iraq', 'Kuwait',
                     'UAE','Jordan', 'Brunei', 'Palestine', 'Oman', 'Syria']

oceanie = ['Australia', 'New Zealand', 'Guam', 'French Polynesia', 'New Caledonia', 'Fiji', 'Papua New Guinea']

autre = ['Diamond Princess', 'CAR']



def attribution_continent (data) :
    data['Continent'] = 'Na'
    data['Continent'].astype('category')
    for i in range (0,len(data.index)) :
        pays = data.index[i]
        
        if pays in amerique :
            data.iloc[i,7] = 'Amerique'
        elif pays in europe_est :
            data.iloc[i,7] = "Europe de l'est"
        elif pays in europe_ouest :
            data.iloc[i,7] = "Europe de l'ouest"
        elif pays in afrique :
            data.iloc[i,7] = "Afrique"
        elif pays in asie :
            data.iloc[i,7] = "Asie"
        elif pays in asie_occidentale :
            data.iloc[i,7] = "Asie occidentale"
        elif pays in oceanie :
            data.iloc[i,7] = "Oceanie"
        elif pays in autre :
            data.iloc[i,7] = "Autres"


