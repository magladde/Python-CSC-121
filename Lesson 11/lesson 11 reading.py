# example 1
daily_temps = {'sun': 68.8, 'mon': 70.2, 'tue': 67.2, 'wed': 71.8, 'thur': 73.2, 'fri': 75.6, 'sat': 74.0}

print('Temperature on Wednesday:', daily_temps['wed'])
print('Temperature on Saturday:', daily_temps['sat'])
print('\n')

# example 2
players ={17: 'David Fox', 25: 'Jerry Rice', 8: 'George Simmons', 51: 'Larry King', 40: 'Tyler Park'}
print(players[17])
print(players[25])
print(players[8])
print(players[51])
print(players[40])
print('Number of players:', len(players))
print('\n')

# example 3
stations = {89.7: 'WCPE', 91.5: 'WUNC', 92.3: 'WKRR', 92.5: 'WYFL'}

print('89.7 FM:', stations[89.7])
print('91.5 FM:', stations[91.5])
print('92.3 FM:', stations[92.3])
print('92.5 FM:', stations[92.5])
print('Number of stations:', len(stations))
print('\n')

# example 4
station_list = [[89.7, 'WCPE'], [91.5, 'WUNC'], [92.3, 'WKRR'], [92.5, 'WYFL']]
stations = dict(station_list)
print('89.7 FM:', stations[89.7])
print('91.5 FM:', stations[91.5])
print('92.3 FM:', stations[92.3])
print('92.5 FM:', stations[92.5])
print('Number of stations:', len(stations))
print('\n')

# example 5
