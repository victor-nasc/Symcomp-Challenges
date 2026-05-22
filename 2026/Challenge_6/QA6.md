# Challenge — Análise de Complexidade

## Enigma

Considere o seguinte algoritmo recursivo em Python:

```python
def misterio(n):
    if n <= 0:
        return 0
    total = 0
    for i in range(n):
        total += i
    return total + misterio(n // 2)
```

Quantas vezes a instrução `total += i` é executada ao todo quando chamamos `misterio(1024)`?

## Resposta

As chamadas recursivas acontecem com:
`n = 1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0 (para)`

O laço `for i in range(n)` executa exatamente `n` vezes em cada chamada.

Total = 1024 + 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1

PG com razao 1/2 com 11 termos:

$$Total = 1024 (1 − (1/2)**11) / (1 − 1/2) = 2048 − 1 = 2047$$

**Resposta:** `2047`
