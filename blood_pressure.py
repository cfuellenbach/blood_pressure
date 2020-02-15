import pandas as pd

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

# initiate input of a new measurement > condensed as list > added to df

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

misc = input('If there was anything special to the measurement itself or the day you measured (eg, a very stressful day in general) please give information here. If not hit return \n> ')

# calculating means of triple measurement

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

bp['date_time'] = pd.to_datetime(bp['date_time'])
