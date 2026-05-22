# Challenge — Imagem

## Enigma

Considere a imagem `logo.png`.

A **entropia de Shannon** mede a quantidade de informação (imprevisibilidade) de uma fonte

- Uma imagem quase toda preta ou branca possui baixa entropia
- Uma imagem cheia de detalhes, texturas e muitos níveis de cinza possui alta entropia, porque os pixels variam bastante.

Para uma imagem em escala de cinza, ela é definida como:

$$H = -\sum_{v=0}^{255} p(v) \cdot \log_2 p(v)$$

onde $p(v)$ é a probabilidade do valor de luminância $v$ ocorrer, ou seja, o número de pixels com aquele valor dividido pelo total de pixels

Para converter cada pixel RGB para luminância, use o padrão **ITU-R BT.601**:

$$L = \lfloor 0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B \rfloor$$

Qual é a entropia de Shannon da imagem `logo.png`, arredondada para 1 casas decimais?

## Resposta

`6.9`
