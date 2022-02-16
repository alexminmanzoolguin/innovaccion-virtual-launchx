planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

user_planet= input('por favor el nombre de un planeta:')

planets_index=planets.index(user_planet)

print('los planetas mas cercanos al sol es:'+user_planet)
print(planets[0:planets_index])

print('los planetas mas lejanos al sol son:'+user_planet)

print(planets[planets_index+1:])