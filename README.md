# txt-to-sql-in-formatter

A lightweight utility that quickly transforms a plain text list into a SQL-ready `IN (...)` clause.  
Um utilitário simples para transformar rapidamente listas em TXT em uma cláusula `IN (...)` pronta para uso em SQL.  
Un utilitaire permettant de transformer rapidement une liste TXT en une clause SQL `IN (...)` prête à l’emploi.

---

## 🇺🇸 English

### Overview
This tool reads a text file (`ids.txt`) containing one value per line and converts it into a single `IN (...)` list ready to paste directly into an SQL query.

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
Ferramenta que lê um arquivo (`ids.txt`) com um valor por linha e transforma tudo em uma única lista `IN (...)`, já formatada para colar direto em uma query SQL.

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
Cet outil lit un fichier (`ids.txt`) contenant une valeur par ligne et transforme le tout en une seule liste `IN (...)` prête à être utilisée dans une requête SQL.

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
