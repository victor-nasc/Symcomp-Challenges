from PIL import Image
import math, collections

img = Image.open("logo.png").convert("RGB")
pixels = list(img.getdata())
n = len(pixels)

gray = [int(0.299*r + 0.587*g + 0.114*b) for r, g, b in pixels]
freq = collections.Counter(gray)
H = -sum((c / n) * math.log2(c / n) for c in freq.values())

print(round(H, 4))