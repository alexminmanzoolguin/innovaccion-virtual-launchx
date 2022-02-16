# Defino mi función
def rocket_parts():
    print('payload, propellant, structure')

print(rocket_parts())

destination= input('ingrese el planeta')
def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth(destination))

