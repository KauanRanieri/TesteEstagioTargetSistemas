def calcular_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

def main():
    indice = 13
    soma = calcular_soma(indice)
    print(f"O valor da variável SOMA é: {soma}")

if __name__ == "__main__":
    main()