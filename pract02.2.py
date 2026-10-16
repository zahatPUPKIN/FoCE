import sys
Time=[]
Airtemp=[]
Windspeed=[]
WCtemp=[]
WCef=[]

x = input("введите номер файла от 1 до 3: ")
if x.isalpha() or int(x)<1 or int(x)>3:
    print("Вы ввели несуществующий номер файла, перезапустите программу ")
    sys.exit()
x = int(x)
with open(f'{x}.WCData.txt', 'r') as file:
    l = file.read().splitlines()

for i in range(2,len(l)):
    Time.append(l[i].split()[0])
    Airtemp.append(l[i].split()[1])
    Windspeed.append(l[i].split()[2])
    

    

ave = round(sum(float(num) for num in WCtemp) / len(WCtemp),1)    
with open(f'{x}.WindChillReport.txt','w') as file2:
    file2.write('Time')
    file2.write(' '*3)
    file2.write('WC Temp')
    file2.write(' '*2)
    file2.write('WC Effect\n')
    file2.write('-'*50)
    file2.write('\n')
    for i in range(len(Time)):
        file2.write(Time[i])
        file2.write(' {: 6}'.format((round(35.74+0.6125*int(Airtemp[i])+(0.4275*int(Airtemp[i])-35.75)*(int(Windspeed[i])**0.16),1))))
        
        file2.write(' {: 7}'.format(round(WCtemp[i] - int(Airtemp[i]),1)))
        
        file2.write('\n')
    
    file2.write('-'*50)    
    file2.write('\n')
    file2.write(f'The average adjusted temperature, based on {len(Time)} observations, was {ave}')







