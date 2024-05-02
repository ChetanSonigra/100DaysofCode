data = []
with open('Day25/weather_data.csv') as f:
    data = f.readlines()
    
print(data)

import csv

with open('Day25/weather_data.csv') as f:
    data = csv.reader(f)
    temperatures = []
    print(data)
    for row in data:
        print(row)
        if row[1]!='temp':
            temperatures.append(int(row[1]))
            
print(temperatures)


import pandas as pd

data_df = pd.read_csv('Day25/weather_data.csv')
print(data_df)
print(data_df["temp"])

data_dict = data_df.to_dict()         # can change dataframe to any data type.
print(data_dict)

temp_list = data_df["temp"].to_list()
print(temp_list)

print(sum(temp_list)/len(temp_list))
print(data_df['temp'].mean())
print(data_df['temp'].max())

#  Getting data of column: 
print(data_df['temp'])
print(data_df.temp)

# Get data in row:
print(data_df[data_df.day=='Monday'])
print(data_df[data_df.temp==data_df.temp.max()])

# convert monday's temperature into feranhite
print(data_df[data_df.day=='Monday'].temp[0]*(9/5)+32)


# create a dataframe from scratch

data_dict = {
    'students': ['Amy','Ram','James'],
    'scores': [76,57,88]
}

data= pd.DataFrame(data_dict)
print(data)
data.to_csv('Day25/students_score.csv')


# Get squirrel count of each color.
central_park_data=pd.read_csv('Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data = central_park_data.value_counts('Primary Fur Color')
print(data)
data.to_csv('Day25/fur_colors.csv')