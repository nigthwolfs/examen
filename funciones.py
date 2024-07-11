import random
import csv
import math

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]

def salario():
    global sueldos
    sueldos = []
    for i in range(10):
        sueldo=random.randint(300000,2500000)
        sueldos.append(sueldo)
    print("Sueldos generados!")

def estadisticas():
    sueldomax=max(sueldos)
    sueldomin=min(sueldos)
    sueldo_prom=sum(sueldos) / len(sueldos)
    sueldomedia = math.prod(sueldos)**(1/len(sueldos))


    print("sueldo mas alto: $"+str(sueldomax))
    print("sueldo mas bajo: $"+str(sueldomin))
    print("promedio sueldos: $"+str(sueldo_prom))
    print("media geometrica: $"+str(sueldomedia))

def clasificar():
    menores = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] < 800000]
    medios = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if 800000 <= sueldos[i] <= 2000000]
    mayores = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] > 2000000]
    
    print("Sueldos menor a $800.000 = ", len(menores))
    for empleado, sueldo in menores:
        print(f"{empleado}: ${sueldo}")
    
    print("Sueldos entre 800000 y 2000000 :", len(medios))
    for empleado, sueldo in medios:
        print(f"{empleado}: ${sueldo}")
    
    print("Sueldos superior a $2000000 :", len(mayores))
    for empleado, sueldo in mayores:
        print(f"{empleado}: ${sueldo}")
    
    total_sueldos = sum(sueldos)
    print("sueldo total : "+str(total_sueldos))


def reporte():
    descuentos = [{"nombre": trabajadores[i], 
                   "sueldo_base": sueldos[i], 
                   "descuento_salud": sueldos[i] * 0.07, 
                   "afp": sueldos[i] * 0.12, 
                   "liquido": sueldos[i] * 0.81} for i in range(len(sueldos))]
    
    print("Nombre empleado  Sueldo Base  Descuento Salud  Descuento AFP  Sueldo Líquido")
    for d in descuentos:
        print(f"{d['nombre']}  ${d['sueldo_base']}  ${d['descuento_salud']:.2f}  ${d['descuento_afp']:.2f}  ${d['sueldo_liquido']:.2f}")
    
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        for d in descuentos:
            writer.writerow([d['nombre'], d['sueldo_base'], d['descuento_salud'], d['descuento_afp'], d['sueldo_liquido']])
    
    print("Reporte exportado a 'reporte_sueldos.csv'")

