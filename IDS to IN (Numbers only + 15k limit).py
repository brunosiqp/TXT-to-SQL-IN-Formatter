import re

entrada = "ids.txt"
tamanho_bloco = 15000

# Lê e limpa os IDs
with open(entrada, "r") as f:
    ids = []
    for linha in f:
        linha = linha.strip()
        if linha:
            numeros = re.findall(r'\d+', linha)  # pega só números
            if numeros:
                ids.append("".join(numeros))  # junta caso tenha mais de um grupo

# Divide em blocos
for i in range(0, len(ids), tamanho_bloco):
    bloco = ids[i:i + tamanho_bloco]
    numero_arquivo = (i // tamanho_bloco) + 1
    nome_saida = f"in{numero_arquivo}.txt"

    conteudo = "(" + ", ".join(bloco) + ")"

    with open(nome_saida, "w") as f:
        f.write(conteudo)

    print(f"Gerado: {nome_saida}")

print("Finalizado, guri. Aulas demais.")