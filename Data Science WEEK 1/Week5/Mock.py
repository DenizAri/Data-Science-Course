import pandas as pd
df = pd.read_csv("MOCK_DATA.csv")
df = df.set_index('Keyword')

#get list of destinations
destlist = df['MOCK_DATA'].tolist()

#turn list into set to make it easier to work with
destination = set(destlist)


city = ['NewYork','Tucson','Rome','Athen','Barcelona','Florance']

#loop to create a csv for each destination
for dest in destination:
    tempdf = df[(df['MOCK_DATA'] == dest)]
    tempdf.to_csv(dest + ".csv")
    print(tempdf.head())
    #print(dest)