import os
import random
from datetime import date, timedelta

import pandas as pd

random.seed(2026)

FLAG = "mtbom"

PRODUCTS = {
    "Eletrônicos": [
        ("Smartphone Samsung Galaxy", 1299),
        ("Fone Bluetooth JBL", 349),
        ("Notebook Dell Inspiron", 3499),
        ("Smartwatch Apple Watch", 2199),
        ("Tablet iPad Air", 4299),
        ("Câmera Canon EOS", 2799),
    ],
    "Roupas": [
        ("Camiseta Polo Lacoste", 259),
        ("Calça Jeans Levi's", 299),
        ("Tênis Nike Air Max", 449),
        ("Jaqueta Couro Premium", 599),
        ("Vestido Floral", 249),
        ("Shorts Esportivo Adidas", 219),
    ],
    "Casa": [
        ("Liquidificador Oster", 299),
        ("Cafeteira Nespresso", 499),
        ("Aspirador Electrolux", 699),
        ("Panela de Pressão Tramontina", 239),
        ("Jogo de Cama 300 Fios", 329),
        ("Tapete Persa Importado", 849),
    ],
    "Livros": [
        ("Clean Code - Robert Martin", 189),
        ("Design Patterns - GoF", 209),
        ("Python Fluente - Ramalho", 199),
        ("O Senhor dos Anéis", 179),
        ("Dom Casmurro - Machado", 169),
        ("Sapiens - Yuval Harari", 179),
    ],
    "Esportes": [
        ("Bicicleta Speed Trek", 3299),
        ("Luva Boxe Everlast", 229),
        ("Raquete Tênis Wilson", 449),
        ("Mochila Hiking Deuter", 399),
        ("Bola Futsal Penalty", 209),
        ("Garrafa Térmica Stanley", 219),
    ],
}

PAYMENT_METHODS = ["credit", "debit", "pix", "boleto"]

flat_products = [
    (cat, name, price)
    for cat, items in PRODUCTS.items()
    for name, price in items
]

N_TOTAL = 50
N_OUTLIERS = len(FLAG)  # 5

# Pre-pick positions for outlier injection (sorted → flag order preserved)
outlier_positions = set(sorted(random.sample(range(1, N_TOTAL + 1), N_OUTLIERS)))

rows = []
outlier_idx = 0
start_date = date(2024, 1, 1)

for i in range(1, N_TOTAL + 1):
    txn_id = f"TXN_{i:02d}"
    customer_id = f"user_{i:02d}"
    _, name, base_price = random.choice(flat_products)
    quantity = random.randint(3, 8)
    price = round(base_price * random.uniform(0.85, 1.15), 2)
    txn_date = start_date + timedelta(days=random.randint(0, 729))

    if i in outlier_positions:
        # ASCII code of each flag character hidden as total_amount
        total_amount = float(ord(FLAG[outlier_idx]))
        outlier_idx += 1
    else:
        total_amount = round(price * quantity, 2)

    rows.append({
        "transaction_id": txn_id,
        "customer_id": customer_id,
        "product": name,
        "total_amount": total_amount,
        "date": txn_date.isoformat(),
    })

df = pd.DataFrame(rows)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transacoes.csv")
df.to_csv(output_path, index=False)
print(f"Dataset gerado: {len(df)} transações  ({N_OUTLIERS} outliers injetados)")
