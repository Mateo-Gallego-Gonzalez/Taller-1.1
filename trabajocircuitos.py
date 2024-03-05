'''Desarrollar un Script en Python que le permita al usuario diseñar un circuito eléctrico a su gusto
    en el cual tenga la posibilidad de digitar valores a sus correspondientes elementos, tal como una fuente de
    voltaje, resistores ya sean en serie o paralelo (permitir dos resistores en paralelo nada más) y por supuesto
    finalizar con una tierra (GND). Finalmente calcular resistencia equivalente, corriente total y voltaje total.
    Recordar alterar las tolerancias resistivas mediante el módulo RANDOM. Obtener un esquema/plano del circuito.
    
    AUTORES: Mateo Gallego Gonzáles - Edison David Arbelaez Jimenez - Santiago Mejía (Soporte en videos)
'''

import random #Importación RANDOM para generar valores al azar/aleatorios

#Importa RANDOM para generar números/valores al azar/aleatorios.

def agregar_resistencia_serie(componentes, valor_resistencia): #Función que recibe valores (valor_resistencia)
    componentes.append(['S', valor_resistencia]) #Mediante una lista, agrega el valor digitado por el usuario (.append - final)

'''Función que recibe valor (valor_resistencia) y, mediante una lista, con .append agrega el valor como un elemento
    final. 'S' indica serie en la lista.
'''

def agregar_resistencia_paralelo(componentes, valor_resistencia1, valor_resistencia2):
    componentes.append(['P', valor_resistencia1, valor_resistencia2])

'''Función que recibe valores (valor_resistencia1 y valor_resistencia2) y, mediante una lista, con .append agrega
     los valores como elementos finales. 'P' indica paralelo en la lista.
'''

def calcular_resistencia_total(componentes):
    resistencia_total = 0
    for componente in componentes:
        if componente[0] == 'S':
            resistencia_total += componente[1]
        elif componente[0] == 'P':
            resistencia1 = componente[1]
            resistencia2 = componente[2]
            resistencia_total += 1 / (1 / resistencia1 + 1 / resistencia2)
    return resistencia_total

'''Función que recibe los valores (componentes). Se inicializa resistencia_total con un valor 0 y se entra en For
    ya que sabemos cuántas veces se repetirá el evento mediante a las decisiones del usuario. Por revisión de los
    elementos de las listas, se evalúa con un if si sus valores van tomando un orden en las posiciones para operar.
    En serie, se hace una "fila" de valores las cuales se sumarán simultáneamente. En paralelo, se evalúan los
    valores acorde a cada posición/índice de la "fila" de valores para aplicar la fórmula de Req. Finalmente
    retorna un valor total de una resistencia equivalente.
'''

def calcular_corriente_resultante(fuente_voltaje, resistencia_total):
    corriente_resultante = fuente_voltaje / resistencia_total
    return corriente_resultante

'''Función que, por medio de entradas como el valor asignado de la fuente y una resistencia equivalente, se aplica
    la Ley de OHM y determina, operando, el valor de la corriente resultante del circuito y lo retorna.
'''

def simular_tolerancias(componentes, tolerancia_porcentaje):
    for componente in componentes:
        if componente[0] == 'S':
            valor_resistencia = componente[1]
            tolerancia = valor_resistencia * tolerancia_porcentaje / 100
            componente[1] += random.uniform(-tolerancia, tolerancia)
        elif componente[0] == 'P':
            valor_resistencia1 = componente[1]
            valor_resistencia2 = componente[2]
            tolerancia1 = valor_resistencia1 * tolerancia_porcentaje / 100
            tolerancia2 = valor_resistencia2 * tolerancia_porcentaje / 100
            componente[1] += random.uniform(-tolerancia1, tolerancia1)
            componente[2] += random.uniform(-tolerancia2, tolerancia2)

'''Función que, por medio de RANDOM, se operan valores aleatorios conservando un porcentaje de tolerancia acorde a
    la operación interna del valor asignado al resistor y el valor aleatorio, esto mediante a las posiciones de la
    lista para continuar con un orden. (Se aclara que tuvimos que consultar esta función en la web... Jajaja).
'''

def representar_circuito(fuente_voltaje, componentes):
    print("Esquema del circuito:")
    print(f"Fuente: (V{fuente_voltaje}V)->", end="")
    for componente in componentes:
        if componente[0] == 'S':
            print(f"-|-RS[{componente[1]:.3f}Ω]-|->", end="")
        elif componente[0] == 'P':
            print(f"-|-RP[{componente[1]:.3f}/{componente[2]:.3f}Ω]-|->", end="")
    print("(GND)")

'''Función que recibe un valor de fuente asignado y el valor de sus elementos elegidos (resistores S ó P). Mediante
    impresiones con formato, se hace un boceto del circuito con símbolos representativos. Identifica por medio de For
    con condicionales agregados si lo que se obtuvo fueron resistores en serie, de ser así obtiene su propia simbología
    al giaul que con resistores en paralelo. Para imprimir, se evalúan los valores que hayan en las posicones de la
    lista, para estipular un orden, también controlando sus decimales a tan solo tres cifras decimales. Finaliza con
    salto de línea.
'''

def obtener_valor_resistencia():
    while True:
        valor_resistencia = input("Digite el valor de la resistencia (con 'K' o 'M' si lo desea): ")
        valor_resistencia = valor_resistencia.upper()
        if valor_resistencia[-1] == 'K':
            valor = float(valor_resistencia[:-1]) * 1000
        elif valor_resistencia[-1] == 'M':
            valor = float(valor_resistencia[:-1]) * 1000000
        else:
            valor = float(valor_resistencia)
        
        if valor > 0:  # Verifica si el valor es positivo
            return valor
        else:
            print("El valor de la resistencia debe ser mayor que cero. Inténtelo de nuevo.")

'''Función que entra, obligadamente a un while para que se sí o sí se evalúe los valores asignados por el usuario
    y que a la hora de digitar una escala de unidad como "K" o "M" se modifique el valor a sus correspondientes
    múltiplicaciones. Utilizamos .upper para conservar la tranquilidad de utilizar tanto mayúsculas como minúsculas.
    Procedemos a evaluar la última posición del valor con un [-1] para hacer énfasis en la escala de unidad y con
    [:-1] se hace una lectura y "asignación" de valor a esa letra/escala de unidad para multiplicarla. También 
    determinamos que el usuario digite correctamente un valor que sea > 0.
'''

if __name__ == "__main__":
    while True:
        fuente_voltaje = float(input("Digite el valor de la fuente del circuito (en voltios): "))
        if fuente_voltaje > 0: #Verifica si el voltaje es positivo
            break
        else:
            print("El voltaje de la fuente debe ser mayor que cero. Inténtelo de nuevo.")

    componentes = []

    while True:
        print("\nMenú de opciones:")
        print("1. Añadir resistencia en serie")
        print("2. Añadir resistencia en paralelo")
        print("3. Cerrar el circuito con tierra (GND)")
        opcion = input("Ingrese la opción deseada (1, 2 o 3): ")

        if opcion == '1':
            valor_resistencia = obtener_valor_resistencia()
            agregar_resistencia_serie(componentes, valor_resistencia)

        elif opcion == '2':
            valor_resistencia1 = obtener_valor_resistencia()
            valor_resistencia2 = obtener_valor_resistencia()
            agregar_resistencia_paralelo(componentes, valor_resistencia1, valor_resistencia2)

        elif opcion == '3':
            break

    simular_tolerancias(componentes, 5)

    resistencia_total = calcular_resistencia_total(componentes)
    corriente_resultante = calcular_corriente_resultante(fuente_voltaje, resistencia_total)

    print("\nResultados:")
    print(f"Resistencia equivalente del circuito: {resistencia_total:.3f}Ω")

    if corriente_resultante < 1:
        print(f"Corriente total en el circuito: {corriente_resultante * 1000:.3f}mA")
    else:
        print(f"Corriente total en el circuito: {corriente_resultante:.3f}A")

    representar_circuito(fuente_voltaje, componentes)

    resistencia_nominal = calcular_resistencia_total(componentes)
    tolerancia_resistiva = max([abs(componente[1] - resistencia_nominal) / resistencia_nominal * 100 for componente in componentes])

    print(f"Tolerancia resistiva del circuito: {tolerancia_resistiva:.2f}%")