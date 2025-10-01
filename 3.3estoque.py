estoque = {
    "Mouse": 10,
    "Teclado": 5,
    "Monitor": 2
}

for produto, quantidade in estoque.items():
    print(produto, quantidade)

for produto, quantidade in estoque.items():
    if quantidade < 3:
        print("Estoque baixo:", produto)
