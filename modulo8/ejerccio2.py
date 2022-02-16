planetas_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planetas_moons.values()
planetas = len(planetas_moons.keys())

print(moons)
print(planetas)

total_moons=0
for moon in moons:
    total_moons=total_moons+moon
average=total_moons/planetas

print(average)