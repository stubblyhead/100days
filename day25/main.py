import pandas

data = pandas.read_csv('weather_data.csv')

print(data.temp.max())

mon_temp = data[data.day == 'Monday'].temp

print((mon_temp*9/5+32))
