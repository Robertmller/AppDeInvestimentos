from utilidades import apresentar_programa
import json
from pathlib import Path


def criar_investimentos_iniciais():
    listaDeInvestimentos = [
        {
            "id": 1,
            "nome": "Pc Gamer",
            "valor": 3000
        },
        {
            "id": 2,
            "nome": "Iphone",
            "valor": 10000
        },
        {
            "id": 3,
            "nome": "Casa",
            "valor": 100000
        },
        {
            "id": 4,
            "nome": "Carro",
            "valor": 50000
        },
        {
            "id": 5,
            "nome": "Xbox",
            "valor": 2000
        }

    ]

    investimentosJson = json.dumps(listaDeInvestimentos)
    Path('investimentos.json').write_text(investimentosJson)


def lerInvestimentosExistentes():
    investimentosJson = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentosJson)
    return investimentos


def exibirInvestimentoTotal():
    investimentos = lerInvestimentosExistentes()
    total = 0
    for investimento in investimentos:
        total = investimento['valor'] + total

    print(f"Total investidos até o momento: R${total:.2f}")


def listarInvestimentos(exibirTodos=False):
    from tabulate import tabulate
    investimentos = lerInvestimentosExistentes()
    listarInvestimentos = []
    for investimento in investimentos:
        listarInvestimentos.append(
            [investimento['id'], investimento['nome'], investimento['valor']])
    print(tabulate(listarInvestimentos, headers=['id', 'nome', 'valor']))


def mostrarMenu():
    print("1 - Criar Investimento")
    print("2 - Listar Investimentos")
    print("3 - Editar Investimento")
    print("4 - Excluir Investimento")
    print("5 - Sair")
    print()
    opcao = int(input("Digite uma opção: "))
    return opcao


if __name__ == '__main__':
    apresentar_programa()
    exibirInvestimentoTotal()
    listarInvestimentos()

    while True:
        opcao = mostrarMenu()
        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            break
        else:
            print("Opção não disponível!")
            break
