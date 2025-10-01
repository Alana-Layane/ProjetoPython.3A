temperaturas = [30, 32, 31, 29, 28]

media = sum(temperaturas) / len(temperaturas)
print("Média:", media)

for temp in temperaturas:
    if temp > 30:
        print("quente")