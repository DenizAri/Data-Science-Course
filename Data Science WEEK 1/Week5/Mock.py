import pandas as pd
holiday = pd.read_csv('MOCK_DATA.csv')
print(holiday)
cities = holiday[['first_name', 'city']]
print(cities)
