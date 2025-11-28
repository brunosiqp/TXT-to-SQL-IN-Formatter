# txt-to-sql-in-formatter

A lightweight utility that converts a plain text file containing one value per line into a single SQL-friendly `IN (...)` list.  
Um utilitário simples que converte um arquivo TXT com um valor por linha em uma lista formatada para `IN (...)` em SQL.  
Un utilitaire léger qui convertit un fichier TXT contenant une valeur par ligne en une liste formatée pour `IN (...)` en SQL.

---

## 🇺🇸 English

### Overview
This tool reads a text file (`ids.txt`) containing one ID per line and generates another file (`in.txt`) with all values formatted inside a single SQL `IN` clause.

### Example

Input (`ids.txt`):
```
100
201
301
4150
13
15151
```

Output (`in.txt`):
```
(100, 201, 301, 4150, 13, 15151)
```

### How to Use
1. Place your `ids.txt` file in the same directory as the script.
2. Run the Python script.
3. The file `in.txt` will be generated automatically.

### Python Script
```python
entrada = "ids.txt"
saida = "in.txt"

with open(entrada, "r") as f:
    nums = [linha.strip() for linha in f if linha.strip()]

resultado = "(" + ", ".join(nums) + ")"

with open(saida, "w") as f:
    f.write(resultado)

print("Arquivo gerado:", saida)
```

### Requirements
- Python 3.6+

### License
MIT License

---

## 🇧🇷 Português (Brasil)

### Descrição
Ferramenta simples que lê um arquivo (`ids.txt`) contendo um valor por linha e gera outro arquivo (`in.txt`) com todos os valores dentro de uma expressão `IN (...)` para SQL.

### Exemplo

Entrada (`ids.txt`):
```
100
201
301
4150
13
15151
```

Saída (`in.txt`):
```
(100, 201, 301, 4150, 13, 15151)
```

### Como Usar
1. Coloque o arquivo `ids.txt` no mesmo diretório do script.
2. Execute o script Python.
3. O arquivo `in.txt` será gerado automaticamente.

### Requisitos
- Python 3.6 ou superior

### Licença
MIT License

---

## 🇫🇷 Français

### Aperçu
Cet outil lit un fichier (`ids.txt`) contenant une valeur par ligne et génère un second fichier (`in.txt`) contenant toutes les valeurs dans une clause SQL `IN (...)`.

### Exemple

Entrée (`ids.txt`) :
```
100
201
301
4150
13
15151
```

Sortie (`in.txt`) :
```
(100, 201, 301, 4150, 13, 15151)
```

### Utilisation
1. Placez `ids.txt` dans le même dossier que le script.
2. Exécutez le script Python.
3. Le fichier `in.txt` sera créé automatiquement.

### Prérequis
- Python 3.6+

### Licence
MIT License
