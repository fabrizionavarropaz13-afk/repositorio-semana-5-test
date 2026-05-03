class Calculadora:

    def sumar(self, *args):
        return sum(args)


calc = Calculadora()

print(calc.sumar(2, 3))        # 2 números
print(calc.sumar(2, 3, 4))     # 3 números
print(calc.sumar(2.5, 3.1))    # decimales

try:
    num = int(input("Ingrese un número: "))
    resultado = 10 / num
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

except ValueError:
    print("Error: Debe ingresar un número válido")

finally:
    print("Fin del programa")

estudiantes = []


estudiantes.append("Luis")
estudiantes.append("Ana")
estudiantes.append("Carlos")

print("Lista de estudiantes:")
for e in estudiantes:
    print(e)


estudiantes.remove("Ana")

print("Después de eliminar:")
for e in estudiantes:
    print(e)