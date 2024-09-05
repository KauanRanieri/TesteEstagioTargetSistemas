import json
import os

def carregar_dados(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def calcular_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        raise ValueError("Não há dados de faturamento para calcular.")

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

def main():
    caminho_arquivo = r'C:\Users\Kauan\Desktop\Teste Estágio - Target Sistemas1\exercicio3\faturamento.json'
    
    try:
        dados = carregar_dados(caminho_arquivo)
        menor_valor, maior_valor, dias_acima_media = calcular_faturamento(dados)

        print(f"Menor valor de faturamento: R${menor_valor:.2f}")
        print(f"Maior valor de faturamento: R${maior_valor:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()