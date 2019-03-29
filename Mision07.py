# Autor: María Fernanda García Gastélum     A01376181
# Completar misión 07

def dividir(dividendo, divisor):
    vecesRestado = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        vecesRestado += 1
    return vecesRestado, dividendo


def encontrarMayor():
    print("\nEscribe los números que quieras para encontrar el mayor.")
    numeros = int(input("Teclea un número [-1 para salir]: "))
    numeroAcumulado = numeros
    if numeros == -1:
        print("No hay valor mayor")
    else:
        while numeros != -1:
            if numeros > numeroAcumulado:
                numeroAcumulado = numeros
                numeros = int(input("Teclea un número [-1 para salir]: "))
            else:
                numeros = int(input("Teclea un número [-1 para salir]: "))
        print("El mayor es:", numeroAcumulado)


def main():
    print("Misión 07. Ciclos While")
    print("Autor: María Fernanda García Gastélum")
    print("Matrícula: A01376181")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")

    opcionSeleccionada = int(input("Teclea tu opción: "))
    while opcionSeleccionada != 3:
        if opcionSeleccionada != 1 and opcionSeleccionada != 2:
            print("ERROR \nTeclea 1, 2 o 3\n")
            print("Misión 07. Ciclos While")
            print("Autor: María Fernanda García Gastélum")
            print("Matrícula: A01376181")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcionSeleccionada = int(input("Teclea tu opción: "))
        else:
            if opcionSeleccionada == 1:
                print("\nCalculando divisiones")
                dividendo = int(input("Dividendo: "))
                divisor = int(input("Divisor: "))
                veces, residuo = dividir(dividendo, divisor)
                print(dividendo, "/", divisor, "=", veces, ", sobra", residuo, "\n")
                print("Misión 07. Ciclos While")
                print("Autor: María Fernanda García Gastélum")
                print("Matrícula: A01376181")
                print("1. Calcular divisiones")
                print("2. Encontrar el mayor")
                print("3. Salir")
                opcionSeleccionada = int(input("Teclea tu opción: "))
            if opcionSeleccionada == 2:
                encontrarMayor()
                print("\nMisión 07. Ciclos While")
                print("Autor: María Fernanda García Gastélum")
                print("Matrícula: A01376181")
                print("1. Calcular divisiones")
                print("2. Encontrar el mayor")
                print("3. Salir")
                opcionSeleccionada = int(input("Teclea tu opción: "))
    print("\nGracias por usar este programa, regresa pronto.")


main()
