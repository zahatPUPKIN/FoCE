x=input("введите номер файла от 0 до 3: ")
with open(f'inmap{x}.dat', 'r') as file:
    l = file.read().splitlines()
    
places = int(l[0].split()[0])
mashtab = float(l[0].split()[1])
distances = (l[1:])
p=1
s=0  

print("Ткачёв Захар")
print("Simple Map Distance Computations")
print("Map scale factor   ",mashtab,"miles per inch")
print(" "*3,"Map"," "*5,"Mileage")
print(" "*3,"Measure"," ","Distance")
print("="*45)
for i in range(places):
    
    x=distances[i]
    a = round(float(distances[i])*mashtab,1)
    print("#",p," "*2,x," "*4,a)
    p+=1
    s+=a
print("="*45)
print("Total Distance:   ",s)

    

