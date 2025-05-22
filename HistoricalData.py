import pandas as pd
from bs4 import BeautifulSoup
import requests

# All UEFA Competitions
years = [1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020]

# Looking for patterns to get all the years matches
def get_matches(year):
    # getting the text
    web = f'https://en.wikipedia.org/wiki/UEFA_Euro_{year}'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    # find_all function will find all the data named with div tag and class 'footballbox'
    matches = soup.find_all('div', class_='footballbox')

    # Making lists to separate home, away teams and the scores
    home = []
    score = []
    away = []

    for match in matches:
       home.append(match.find('th', class_='fhome').get_text())
       score.append(match.find('th', class_='fscore').get_text())
       away.append(match.find('th', class_='faway').get_text())

    # make a dictionary so that home score and away data is all in one place uniquely identified by the keys
    dict_football = {'home': home,
                     'score': score,
                     'away': away}

    # Make a dataframe (rows and column)
    df_football = pd.DataFrame(dict_football)
    df_football['Year'] = year  # column to differentiate at what year the matches were played

    return df_football

# Historical Data from 1960-2020
euro = [get_matches(year) for year in years]
df_euro = pd.concat(euro, ignore_index=True)  # Merge all the data in one dataframe
df_euro.to_csv('euro_historical_data.csv', index=False)


# Fixture for Euro 2024
df_fixture = get_matches('2024')

# Adding a Match column with incremental match numbers starting from 1
df_fixture['Match'] = range(1, len(df_fixture) + 1)

# Drop score column as we need to predict
df_fixture.drop('score', axis=1, inplace=True)
df_fixture.to_csv('euro_2024_fixtures.csv', index=False)



