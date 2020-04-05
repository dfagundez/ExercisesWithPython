# Inicializo todas las variables a utilizar
SUELDOJR = 30000
EXTRAJR = SUELDOJR / 25 / 8 * 1.2
SUELDOSSR = 45000
EXTRASSR = SUELDOSSR / 25 / 8 * 1.2
SUELDOSR = 60000
EXTRASR = SUELDOSR / 25 / 8 * 1.2
totalSueldosJr = 0
totalSueldosSsr = 0
totalSueldosSr = 0
totalSueldos = 0
sueldoPromedio = 0
proporcionalHijo = 500
antiguedad = 0
horasExtras = 0
mayorSueldo = 0
sueldo = 0
extras = 0
contador = 0

# Consulto cual es el sector del empleado ya que se una de las respuestas se utiliza para salir del sistema.
print('Sistema para calcular sueldo de empleados.')
sector = int(input("Ingrese sector del empleado a regitrar:\n 1) Ventas\n 2) Contaduria\n 3) Logistica y "
                   "Disbribucion\n 4) Personal\n 0) Salir\n"))

# Inicializo calculos si el sector no es el valor de salida.
while sector != 0:
    # Antes de continuar valido que se ingrese un sector valido.
    if sector > 5 or sector < 0:
        print("Ingreso un sector invalido.")
        sector = input("Porfavor ingrese sector del empleado a regitrar:\n 1) Ventas\n 2) Contaduria\n 3) Logistica y "
                       "Disbribucion\n 4) Personal\n 0) Salir\n")

    # Solicito el resto de los datos necesarios para realizar los calculos y mostrar los resultados.
    empleado = input("Ingreso nombre del empleado: ")
    categoria = int(input("Ingrese categoria a la que pertenece:\n 1) Jr\n 2) Ssr\n 3) Sr\n"))

    # Solicito nuevamente la categoria en caso que se haya ingresado una invalida.
    if categoria > 3 or categoria < 1:
        print("Ingreso una categoria invalida")
        categoria = int(input("> Porfavor numero de categoria al que pertenece:\n 1. Jr\n 2. Ssr\n 3. Sr\n"))

    # Continuo con la solicitud de datos
    cantHijos = int(input('Catnidad de hijos en edad escolar: '))
    antiguedad = int(input('Años de antiguedad: '))

    # Si el sector es de Logistica y Disbribucion, consulto las horas extras trabajadas.
    if sector == 3:
        horasExtras = int(input("Horas extras trabajadas: "))

    # Realizo calculo de proporcional por hijos
    plusHijos = proporcionalHijo * cantHijos

    if categoria == 1:
        extras = horasExtras * EXTRAJR
        antiguedad = antiguedad * (SUELDOJR * 0.08)
        sueldo = SUELDOJR + plusHijos + antiguedad + extras
        totalSueldosJr = sueldo + totalSueldosJr
        totalSueldos = sueldo + totalSueldos
    elif categoria == 2:
        extras = horasExtras * EXTRASSR
        antiguedad = antiguedad * (SUELDOSSR * 0.08)
        sueldo = SUELDOSSR + plusHijos + antiguedad + extras
        totalSueldosSsr = sueldo + totalSueldosSsr
        totalSueldos = sueldo + totalSueldos
    elif categoria == 3:
        extras = horasExtras * EXTRASR
        antiguedad = antiguedad * (SUELDOSR * 0.08)
        sueldo = SUELDOSR + plusHijos + antiguedad + extras
        totalSueldosSr = sueldo + totalSueldosSr
        totalSueldos = sueldo + totalSueldos

    # Guardo en una variable cual es el sueldo mayor comparando cada ingreso con el anterior mas grande.
    if sueldo > mayorSueldo:
        mayorSueldo = sueldo
        eMayorSueldo = f"{empleado} es el empleado con el mayor sueldo, siendo este de $ {mayorSueldo}"

    # Como ya paso todas las validaciones, inicio el contador de empleados.
    contador = contador + 1

    # Confirmo registro.
    print('El empleado se registro correctamente.')
    print('\n')

    # Solicito nuevo empleado a registrar o la opcion para salir.
    sector = int(input("Ingreso sector del siguiente empleado a regitrar:\n 1) Ventas\n 2) Contaduria\n 3) Logistica "
                       "y Disbribucion\n 4) Personal\n 0) Salir\n"))

# Una vez finalizado las operaciones, calculo el sueldo promedio.
sueldoPromedio = totalSueldos / contador

# Imprimo los resultados en pantalla.
print("Resultados:")
print(eMayorSueldo)
print(f"Total a pagar de sueldos Junior: $ {totalSueldosJr}")
print(f"Total a pagar de sueldos Semi Senior: $ {totalSueldosSsr}")
print(f"Total a pagar de sueldos Senior: $ {totalSueldosSr}")
print(f'Sueldo promedio de la empresa: $ {sueldoPromedio}')
print(f"Cantidad de empleados: {contador}")
print(f'Total a abonar por la compañía: $ {totalSueldos}')