def variable_length(*args):
    print(args)

print(variable_length('one','two'))


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'


print(sequence_time(4,14,18))

print(sequence_time(4,14,48))


def variable_length(**kwargs):
    print(kwargs)

print(variable_length(tanks=1, day='Wednesday', pilots=3))

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

print(crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins'))