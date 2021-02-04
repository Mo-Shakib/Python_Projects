# Get live covid information
# Author: Mohammad Shakib
from covid import Covid #https://pypi.org/project/covid/
covid = Covid()
countryName = input('Enter country name: ')
try:
    cases = covid.get_status_by_country_name(countryName)
    print(f'Country: {cases["country"]}\nConfirmed: {cases["confirmed"]}\
        \nActive: {cases["active"]}\nDeaths: {cases["deaths"]}\nRecovered: {cases["recovered"]}')
except:
    print('Please try again')
