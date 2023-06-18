dicio_gabarito = {1: "d", 2: "a", 3: "c", 4: "b", 5: "a", 6: "d", 7: "c", 8: "c", 9: "a", 10: "b"}
# A quantidade de itens pode ser alterada, porém, a estrutura de dict deve ser mantida "alternativa: resposta"
corretas = {}
erradas = {}

print("Corretor de provas, para cada questão digite A, B, C ou D \n")

for i in range(1, len(dicio_gabarito) + 1):  # A soma de 1 ao len se deve ao fato da contagem do range começar em 1
    # Itera sobre o range relativo à quantidade de itens em dicio_gabarito
    resposta = (input(f"Questão {i}, resposta: ")).lower()  # recebe a alternativa e converte e minúscula
    confere = {i: resposta}  # dicionário temporário para conferência
    if confere[i] == dicio_gabarito[i]:
        # Confere se o dicionário temporário é igual ao gabarito, se sim, adiciona as corretas
        corretas[i] = resposta
    else:  # Caso não, adiciona as incorretas
        erradas[i] = resposta

"""
O programa não exibe quais foram as questões corretas
para exibir as questôes corretas deve-se imprimir o dict corretas

print(corretas) # Para exibir as questões acertadas
print(erradas) # Para exibir as questões erradas
"""
print("\n", "="*30, "\n")
print(f"Pontuação final: {len(corretas)}")
print("\n", "="*30, "\n")
