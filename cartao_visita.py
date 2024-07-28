class CartaoVisita:
    def __init__(self, nome, cargo, empresa, endereco, email, telefone, **kwargs):
        self.nome = nome
        self.cargo = cargo
        self.empresa = empresa
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.outros = kwargs

    def exibir_cartao(self):
        print("------------------------------")
        print(f"{self.nome}")
        print(f"{self.cargo} na {self.empresa}")
        print(f"Endereço: {self.endereco}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        for key, value in self.outros.items():
            print(f"{key.capitalize()}: {value}")
        print("------------------------------")

def criar_cartao():
    nome = input("Digite seu nome: ")
    cargo = input("Digite seu cargo: ")
    empresa = input("Digite o nome da empresa: ")
    endereco = input("Digite seu endereço: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    num_opcionais = int(input("Quantas informações opcionais você deseja adicionar? "))
    outros = {}
    for i in range(num_opcionais):
        chave = input("Digite o nome da informação opcional: ")
        valor = input(f"Digite a informação para {chave}: ")
        outros[chave] = valor

    return CartaoVisita(nome, cargo, empresa, endereco, email, telefone, **outros)

def salvar_cartao(cartao):
    nome_arquivo = input("Digite o nome do arquivo que deseja salvar o cartão: ")
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(f'Nome: {cartao.nome}\n')
        arquivo.write(f'Cargo: {cartao.cargo}\n')
        arquivo.write(f'Empresa: {cartao.empresa}\n')
        arquivo.write(f'Endereço: {cartao.endereco}\n')
        arquivo.write(f'Email: {cartao.email}\n')
        arquivo.write(f'Telefone: {cartao.telefone}\n')
        for chave, valor in cartao.outros.items():
            arquivo.write(f'{chave.capitalize()}: {valor}')

def main():
    print("Bem-vindo ao criador de cartão de visita digital!")
    cartao = criar_cartao()
    cartao.exibir_cartao()
    salvar = input("Deseja salvar o cartão de visita? (S/N): ")
    if salvar.upper() == 'S':
        salvar_cartao(cartao)
        print("Cartão de visita salvo com sucesso!")
    else:
        print("Cartão de visita não foi salvo.")

if __name__ == "__main__":
    main()