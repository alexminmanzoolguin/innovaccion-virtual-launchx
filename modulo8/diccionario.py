name = 'Earth'
moons = 1

print(name,moons)

earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

print(earth_name,earth_moons)
print(jupiter_name,jupiter_moons)

planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet)

print(planet.get('name'))

#wibble = planet.get('wibble') # Regresa None
#wibble = planet['wibble'] # Arroja un KeyError

planet.update({'name': 'Makemake'})

print(planet)

# Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79


print(planet)

planet['orbital period'] = 4333

print(planet)

planet.pop('orbital period')

print(planet)

# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet)

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')