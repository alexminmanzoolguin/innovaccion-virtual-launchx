
print("tanque")

def tanques(tanque1,tanque2,tanque3):
    total_tanque=(tanque1+tanque2+tanque3)/3
    return f"""el reporte es :
    total_tanque: {total_tanque}%
    tanque1:{tanque1}%
    tanque2: {tanque2}%
    tanque3:{tanque3}%"""

print(tanques(80,70,75))

print("promedio")

def promedio(values):
     total=sum(values)
     numero=len(values)
     return total/ numero

print(promedio([80,85,81]))


print("reporte del tanque")

def repor_tanques(tanque1,tanque2,tanque3):
    return f"""el reporte es :
    total_average: {promedio([tanque1,tanque2,tanque3])}%
    tanque1:{tanque1}%
    tanque2: {tanque2}%
    tanque3:{tanque3}%"""

print(repor_tanques(88, 76, 70))
