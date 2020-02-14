import pandas as pd
col_names = [
    'date','time',
    'sys_1','dis_1','puls_1',
    'sys_2','dis_2','puls_2',
    'sys_3','dis_3','puls_3',
    'mean_sys','mean_dis','mean_puls',
    'misc'
    ]
bp = pd.DataFrame(columns=col_names)
new_measurement = []
print(bp)
date = input('Please input the date you measured you blood pressure in format dd/mm/yyyy and hit return \n>')
time = input('Please input the time you measured you blood pressure in format hh:mm and hit return \n>')

sys_1 = int(input('Please input the systolic blood pressure of your first of three measurements and hit return \n>'))
dis_1 = int(input('Please input the distolic blood pressure of your first of three measurements and hit return \n>'))
puls_1 = int(input('Please input the puls of your first of three measurements and hit return \n>'))

sys_2 = int(input('Please input the systolic blood pressure of your second of three measurements and hit return \n>'))
dis_2 = int(input('Please input the distolic blood pressure of your second of three measurements and hit return \n>'))
puls_2 = int(input('Please input the puls of your second of three measurements and hit return \n>'))

sys_3 = int(input('Please input the systolic blood pressure of your third of three measurements and hit return \n>'))
dis_3 = int(input('Please input the distolic blood pressure of your thrid of three measurements and hit return \n>'))
puls_3 = int(input('Please input the puls of your third of three measurements and hit return \n>'))

misc = input('If there was anything special to the measurement itself or the day you measured (eg, a very stressful day in general) please give information here. If not hit return \n> ')

mean_sys = (sys_1 + sys_2 + sys_3) / 3
mean_dis = (dis_1 + dis_2 + dis_3) / 3
mean_puls = (puls_1 + puls_2 + puls_3) / 3

new_measurement.extend((date,time,sys_1,dis_1,puls_1,sys_2,dis_2,puls_2,sys_3,dis_3,puls_3,mean_sys, mean_dis, mean_puls,misc))
bp.loc[len(bp)] = new_measurement
