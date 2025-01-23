import pandas

sq = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250121.csv')

black_squirrel_count = len(sq[sq['Primary Fur Color'] == 'Black'])
gray_squirrel_count = len(sq[sq['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(sq[sq['Primary Fur Color'] == 'Cinnamon'])

data_dict = { 'fur color': ['Black', 'Gray', 'Cinnamon'],
              'count': [black_squirrel_count, gray_squirrel_count, cinnamon_squirrel_count]
            }

pandas.DataFrame(data_dict).to_csv('squirrel_count.csv')