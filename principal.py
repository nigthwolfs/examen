import os 
os.system('cls')
from funciones import salario, estadisticas, clasificar,reporte
op=1
ban=0
while(op!=5):
    print("""
reporte trabajadores
1: Asignar Sueldos
2: Clasificar Sueldos
3: Ver Estadisticas
4: Reporte Sueldos
5: Salir del programa
""")
    op=input("seleccione opcion: ")
    if op == '1':
        salario()
    elif op == '2':
        clasificar()
    elif op == '3':
        estadisticas()
    elif op == '4':
        reporte()
    elif op == '5':
        print(""" Saliendo del sistema
              desarrollado por Angello Pessini
              RUT : 20.242.296-9
              """)
        break
    else:
        print("Opcion no valida, intente nuevamente...")