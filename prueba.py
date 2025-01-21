
#Ejercicio1
def es_par_impar(numero):
    return numero % 2 == 0

def imprimir_pares_impares(numero):
    if es_par_impar(numero):
        for i in range(numero, -1, -2):
            print(i)
    else:
        for i in range(numero, 0, -2):
            print(i)
#Ejercicio2
class Persona:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad
def leer_personas():
    PERSONAS = []
    for i in range(50):
        while True:
            sexo = input(f"Ingrese el sexo de la persona {i + 1} (M/F): ").strip().upper()
            if sexo in ['M', 'F']:
                break
            else:
                print("Por favor, ingrese 'M' para masculino o 'F' para femenino.")
        
        while True:
            try:
                edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
                if edad > 0:  # Edad debe ser positiva
                    break
                else:
                    print("La edad debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese una edad válida.")
        
        PERSONAS.append(Persona(sexo, edad))
    return PERSONAS


def mostrar_resultados(PERSONAS):
    mayores_edad = 0
    menores_edad = 0
    hombres_mayores = 0
    mujeres_menores = 0
    mujeres_totales = 0
    
    for persona in PERSONAS:
        if persona.edad >= 18:
            mayores_edad += 1
            if persona.sexo == 'M':
                hombres_mayores += 1
        else:
            menores_edad += 1
            if persona.sexo == 'F':
                mujeres_menores += 1
        if persona.sexo == 'F':
            mujeres_totales += 1
    
    porcentaje_mayores_edad = (mayores_edad / 50) * 100
    porcentaje_mujeres = (mujeres_totales / 50) * 100

    print(f"\nResultados de la clasificación de personas:")
    print(f"a. Cantidad de personas mayores de edad: {mayores_edad}")
    print(f"b. Cantidad de personas menores de edad: {menores_edad}")
    print(f"c. Cantidad de personas masculinas mayores de edad: {hombres_mayores}")
    print(f"d. Cantidad de personas femeninas menores de edad: {mujeres_menores}")
    print(f"e. Porcentaje de personas mayores de edad: {porcentaje_mayores_edad:.2f}%")
    print(f"f. Porcentaje de mujeres respecto al total de personas: {porcentaje_mujeres:.2f}%")

#Ejercicio3 
def calcular_sueldo(horas_trabajadas, tarifa):
    if horas_trabajadas > 40:
        horas_extra = horas_trabajadas - 40
        tarifa_extra = tarifa * 1.5  
        sueldo = (40 * tarifa) + (horas_extra * tarifa_extra)
    else:
        sueldo = horas_trabajadas * tarifa
    return sueldo

#Test
def main():
    print("===Ejercicio1===")
    LEER_NUMERO = int(input("Ingrese un número entero: "))
    imprimir_pares_impares(LEER_NUMERO)
    print("===Ejercicio2===")
    PERSONAS = leer_personas()  
    mostrar_resultados(PERSONAS)
    print("===Ejercicio3===")
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    tarifa = float(input("Ingrese la tarifa por hora en euros: "))
    sueldo = calcular_sueldo(horas_trabajadas, tarifa)
    print(f"El sueldo recibido es: {sueldo:.2f} Euros.")
    
    
if __name__ == "__main__":
    main()
