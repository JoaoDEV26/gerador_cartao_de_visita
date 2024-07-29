# Cartão de Visita Digital

Este projeto permite criar, exibir e salvar um cartão de visita digital utilizando a linguagem Python.


## Funcionalidades

Criação de um cartão de visita com informações básicas e opcionais.
Exibição do cartão de visita no console.
Salvamento do cartão de visita em um arquivo de texto.
Estrutura do Código
O código é composto por uma classe CartaoVisita e três funções principais: `criar_cartao()`,`salvar_cartao(cartao)`, e `main()`.

## Classe CartaoVisita
A classe `CartaoVisita` é responsável por armazenar as informações do cartão de visita e exibi-las no console.

#### Atributos

- *`nome`: Nome do titular do cartão.*
- *`cargo`: Cargo do titular.*
- *`empresa`: Nome da empresa.*
- *`endereco`: Endereço da empresa ou do titular.*
- *`email`: E-mail do titular.*
- *`telefone`: Telefone de contato.*
- *`outros`: Informações adicionais opcionais.*

#### Métodos

*`__init__(self, nome, cargo, empresa, endereco, email, telefone, **kwargs)`: Construtor que inicializa os atributos do cartão.*
*`exibir_cartao(self)`: Método para exibir o cartão de visita no console.*


### Funções 

*`criar_cartao()`: Função que solicita ao usuário as informações para criar um novo cartão de visita.*
*`salvar_cartao(cartao)`: Função que salva as informações do cartão de visita em um arquivo de texto.*
*`main()`: Função principal que coordena a criação, exibição e salvamento do cartão de visita.*

## Como Executar
1. **Certifique-se de ter o Python instalado em seu sistema.**

2. **Salve o código em um arquivo com a extensão .py, por exemplo, cartao_visita.py.**

3. **Execute o arquivo Python:**
```bash
python cartao_visita.py
```

4. **Siga as instruções no console para inserir as informações do cartão de visita.**

5. **Após criar o cartão, escolha se deseja salvá-lo em um arquivo de texto.**

## Exemplo de Uso
```python
if __name__ == "__main__":
    main()
```
Ao executar o código, o usuário será guiado para inserir suas informações e, opcionalmente, salvar o cartão de visita em um arquivo de texto.

## Autor

Este projeto foi desenvolvido por JoãoDEV26.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
