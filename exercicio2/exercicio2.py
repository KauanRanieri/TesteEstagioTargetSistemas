import math

def e_numero_fibonacci(n):
    if n < 0:
        return False
    
    def e_quadrado_perfeito(x):
        if x < 0:
            return False
        s = int(math.sqrt(x))
        return s * s == x

    return e_quadrado_perfeito(5 * n * n + 4) or e_quadrado_perfeito(5 * n * n - 4)

def principal():
    try:
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        
        if e_numero_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    principal()