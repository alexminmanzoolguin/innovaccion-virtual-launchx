from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime('Arrival: %A %H:%M')
print(arrival_time())
print(arrival_time(hours=0))



destination= input('ingrese el planeta')

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time(destination))
print(arrival_time(destination,hours=0.13))