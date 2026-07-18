cadastro_produtos = [
    {"nome": "Mouse", "preco": 45.0},
    {"nome": "Teclado", "preco": 89.0},
]

cadastro_produtos.append({"nome": "Monitor", "preco": 350.0})
cadastro_produtos.append({"nome": "Headphone", "preco": 500.0})
cadastro_produtos.append({"nome": "mouse-pad", "preco": 90.0 })

for item in cadastro_produtos:
    print(f"Produto: {item['nome']}, Preço: R$ {item['preco']:.2f}") 
    