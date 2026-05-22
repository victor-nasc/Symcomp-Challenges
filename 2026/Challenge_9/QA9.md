# Challenge — Validação de CNPJ

## Enigma

algoritmo

**Primeiro dígito (d1):**
1. Multiplique os 12 primeiros dígitos pelos pesos `5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2`
2. Some todos os produtos
3. Calcule `resto = soma % 11`
4. Se `resto < 2` => `d1 = 0`; caso contrário => `d1 = 11 − resto`

**Segundo dígito (d2):**
1. Repita com os 13 dígitos (incluindo d1) e pesos `6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2`
2. Mesma regra para o resto

Qual os numeros faltantes de CNPJ: `11.222.333/0001-??`

## Resposta

Dígitos base: `1 1 2 2 2 3 3 3 0 0 0 1`

**Cálculo de d1:**
```
Pesos:   5  4  3  2  9  8  7  6  5  4  3  2
Dígitos: 1  1  2  2  2  3  3  3  0  0  0  1
Produto: 5  4  6  4 18 24 21 18  0  0  0  2  =>  Soma = 102
resto = 102 % 11 = 3  =>  d1 = 11 − 3 = 8
```

**Cálculo de d2:**
```
Pesos:   6  5  4  3  2  9  8  7  6  5  4  3  2
Dígitos: 1  1  2  2  2  3  3  3  0  0  0  1  8
Produto: 6  5  8  6  4 27 24 21  0  0  0  3 16  =>  Soma = 120
resto = 120 % 11 = 10  =>  d2 = 11 − 10 = 1
```

**Resposta:** `81`
