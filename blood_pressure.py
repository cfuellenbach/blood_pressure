import pandas as pd
from pathlib import Path

if Path('data.csv').is_file() == False:
    col_names = [
        'date_time',
        'sys_1', 'dis_1', 'puls_1',
        'sys_2', 'dis_2', 'puls_2',
        'sys_3', 'dis_3', 'puls_3',
        'mean_sys', 'mean_dis', 'mean_puls',
        'misc'
        ]

    bp = pd.DataFrame(columns=col_names)

# change columns to correct dtypes
    for i in range(1, 13):
        bp[col_names[i]] = pd.to_numeric(bp[col_names[i]])   

else:
    bp = pd.read_csv('data.csv') 

# initiate input of a new measurement > condensed as list > added to df

def measurement():
    new_measurement = []
    date_time = input('Please input the date you measured you blood pressure in format yyyy/mm/dd and hit return \n\n> ')
    date_time = date_time + ', ' + input('Please input the time you measured you blood pressure in format hh:mm and hit return \n\n> ')
    
    sys_1 = int(input('Please input the systolic blood pressure of your first of three measurements and hit return \n\n> '))
    dis_1 = int(input('Please input the distolic blood pressure of your first of three measurements and hit return \n\n> '))
    puls_1 = int(input('Please input the puls of your first of three measurements and hit return \n\n> '))
    
    sys_2 = int(input('Please input the systolic blood pressure of your second of three measurements and hit return \n\n> '))
    dis_2 = int(input('Please input the distolic blood pressure of your second of three measurements and hit return \n\n> '))
    puls_2 = int(input('Please input the puls of your second of three measurements and hit return \n\n> '))
    
    sys_3 = int(input('Please input the systolic blood pressure of your third of three measurements and hit return \n\n> '))
    dis_3 = int(input('Please input the distolic blood pressure of your thrid of three measurements and hit return \n\n> '))
    puls_3 = int(input('Please input the puls of your third of three measurements and hit return \n\n> '))
    
    misc = input('If there was anything special to the measurement itself or the day you measured (eg, a very stressful day at work) please give information here. If not hit return \n> ')
    
    # calculating means of measurements
    
    mean_sys = round((sys_1 + sys_2 + sys_3) / 3)  # make dynamic in case there are less than 3 measurements
    mean_dis = round((dis_1 + dis_2 + dis_3) / 3)
    mean_puls = round((puls_1 + puls_2 + puls_3) / 3)
    
    # adding new measurement to df as row
    
    new_measurement.extend(
        (date_time,
          sys_1, dis_1, puls_1,
          sys_2, dis_2, puls_2,
          sys_3, dis_3, puls_3,
          mean_sys, mean_dis, mean_puls,
          misc)
        )
    bp.loc[len(bp)] = new_measurement
    
    # change to date_time information to date_time format
    
    bp['date_time'] = pd.to_datetime(bp['date_time'])
    
    bp.to_csv('data.csv', index = False)
    print(bp)

# Initiate menu

ans = 0
while ans == 0:
    print('''What would you like to do?
          
          1. Input new measurement
          2. See table of older measurements
          3. Plot data (to come)
          4. Get information on blood presure (to come)
          5. Exit program''')
    ans = int(input('Please give number of your selection:\n>>> '))
    if ans == 1:
        measurement()
    elif ans == 2:
        print(bp)
        ans = 0
    elif ans == 3:
        print('Feature to be implemented in future. Please choose again.')
    elif ans == 4:
        print('Feature to be implemnted in future. Please choose again.')
    elif ans == 5:
        print('Until next time')
