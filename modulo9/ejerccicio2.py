def mision(prelanzaminto,tiempodevuelo,destino,tanqueexterno,tanqueinterno):
    return f"""
    Mision to {destino}
    total tiempo vuelo:{prelanzaminto+tiempodevuelo} minutos
    total de gasolina:{tanqueexterno+tanqueinterno} gallons """

print(mision(14,51,"Moon", 200000, 300000))


def mision_report(destino,*minutos,**reservacion):
    return f"""
    Mision to {destino}
    total travel tiempo:{sum(minutos)} minutos
    total del viaje:{sum(reservacion.values())}"""

print(mision_report("Moon",10,15,51,main=300000,external=200000))


def mision_reportes(destino,*minutos,**reservacion):
    main_report= f"""
    Mision to {destino}
    total travel tiempo:{sum(minutos)} minutos
    total del viaje:{sum(reservacion.values())}"""

    for talk_name,gallons in reservacion.items():
        main_report+= f"{talk_name} tank--> {gallons} gallons left\n"

    return main_report

print(mision_reportes("Moon",8,11,55,main=300000,external=200000))