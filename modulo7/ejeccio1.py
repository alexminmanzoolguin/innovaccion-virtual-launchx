new_planet=input('coloque los nuevos planetas')
planets=[]

while new_planet.lower() !='done':
    if new_planet:
        planets.append(new_planet)
        new_planet=input('enter a new planet')

print(planets)