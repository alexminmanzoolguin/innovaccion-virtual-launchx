distance=int(input('ingresa la distancia'))
speed=int(input('ingresa la velocidad'))   
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
print(days_to_complete(distance, speed))
print(round(days_to_complete(distance, speed)))