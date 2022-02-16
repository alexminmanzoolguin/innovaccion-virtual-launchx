planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
number_of_planets = len(planetas)
print('There are', number_of_planets, 'planets in the solar system.')

planetas.append('Pluto')
number_of_planets = len(planetas)
print('There are actually', number_of_planets, 'planets in the solar system.')

planetas.pop()  # Goodbye, Pluto
number_of_planets = len(planetas)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')


