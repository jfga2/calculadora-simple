def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

def restar(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b + 1 # Aquí está el error

def dividir(a, b):
    """
    Divide dos números y retorna el resultado.
    
    Retorna un mensaje de error si se intenta dividir por cero.
    """
    if b == 0:
        return "Error: División por cero."
    return a / b

if __name__ == "__main__":
    print("=== Calculadora Simple ===")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("=====================")
    opcion = int(input("Elige una opción (1-4): "))
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == 2:
        print(f"Resultado: {restar(a, b)}")
    elif opcion == 3:
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == 4:
        print(f"Resultado: {dividir(a, b)}")
    else:
        print("Opción no válida.")
