import pandas as pd

dados = {
    "data": [
        "2025-01-05", "2025-01-10", "2025-01-15", "2025-02-03",
        "2025-02-12", "2025-02-20", "2025-03-02", "2025-03-11",
        "2025-03-18", "2025-04-05", "2025-04-14", "2025-04-25",
        "2025-05-03", "2025-05-10", "2025-05-22", "2025-06-01",
        "2025-06-13", "2025-06-24", "2025-07-05", "2025-07-17",
        "2025-07-28", "2025-08-04", "2025-08-15", "2025-08-26",
        "2025-09-02", "2025-09-14", "2025-09-25", "2025-10-06",
        "2025-10-18", "2025-10-29"
    ],
    "loja": [
        "Centro", "Shopping", "Centro", "Norte", "Shopping",
        "Sul", "Centro", "Norte", "Shopping", "Sul",
        "Centro", "Norte", "Shopping", "Sul", "Centro",
        "Norte", "Shopping", "Sul", "Centro", "Norte",
        "Shopping", "Sul", "Centro", "Norte", "Shopping",
        "Sul", "Centro", "Norte", "Shopping", "Sul"
    ],
    "produto": [
        "Notebook", "Mouse", "Teclado", "Monitor", "Notebook",
        "Mouse", "Teclado", "Monitor", "Notebook", "Mouse",
        "Teclado", "Monitor", "Notebook", "Mouse", "Teclado",
        "Monitor", "Notebook", "Mouse", "Teclado", "Monitor",
        "Notebook", "Mouse", "Teclado", "Monitor", "Notebook",
        "Mouse", "Teclado", "Monitor", "Notebook", "Mouse"
    ],
    "categoria": [
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios", "Acessórios", "Informática",
        "Informática", "Acessórios"
    ],
    "regiao": [
        "Sudeste", "Sudeste", "Sudeste", "Norte", "Sudeste",
        "Sul", "Sudeste", "Norte", "Sudeste", "Sul",
        "Sudeste", "Norte", "Sudeste", "Sul", "Sudeste",
        "Norte", "Sudeste", "Sul", "Sudeste", "Norte",
        "Sudeste", "Sul", "Sudeste", "Norte", "Sudeste",
        "Sul", "Sudeste", "Norte", "Sudeste", "Sul"
    ],
    "quantidade": [
        2, 10, 7, 3, 1,
        15, 8, 4, 2, 12,
        6, 5, 3, 18, 9,
        4, 2, 20, 10, 3,
        1, 14, 7, 5, 2,
        16, 8, 4, 3, 11
    ],
    "preco_unitario": [
        3500, 80, 150, 1200, 3500,
        80, 150, 1200, 3500, 80,
        150, 1200, 3500, 80, 150,
        1200, 3500, 80, 150, 1200,
        3500, 80, 150, 1200, 3500,
        80, 150, 1200, 3500, 80
    ]
}

df = pd.DataFrame(dados)

df.to_csv("vendas.csv", index=False)

print("Arquivo vendas.csv criado!")