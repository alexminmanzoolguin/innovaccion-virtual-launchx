print("datos:")
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

print("tilulo:")
title= f'datos de gravedad sobre{name}'
print(title)

print("planilla")
print(title)
hechos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity* 1000} m/s2 
"""
print(hechos)


print("union de ambos")
print(title)
template= f"""{title.title()}{hechos}"""
print(hechos)

print("nuevo planeta")

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

titulo = f'datos de gravedad sobre {nombre}'

hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad} m/s2 
"""

new_template = f"""{title.title()} 
{hechos} 
""" 
print(hechos)


print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))

