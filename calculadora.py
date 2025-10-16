import math

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz(self, x):
        if x < 0:
            raise ValueError("Não existe raiz real de número negativo.")
        return math.sqrt(x)

    def media(self, lista):
        if not lista:
            raise ValueError("A lista está vazia.")
        return sum(lista) / len(lista)

    def modulo(self, x):
        return abs(x)

    def percentual(self, parte, total):
        if total == 0:
            raise ValueError("Total não pode ser zero.")
        return (parte / total) * 100
