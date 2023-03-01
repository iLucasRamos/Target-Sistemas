import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] != 0.0]

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

menor_valor = min(faturamento_diario)

maior_valor = max(faturamento_diario)

dias_acima_media = sum([1 for dia in faturamento_diario if dia > media_mensal])

print(f"Menor valor de faturamento diário: {menor_valor}")
print(f"Maior valor de faturamento diário: {maior_valor}")
print(
    f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
