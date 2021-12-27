import json
from pathlib import Path


def apresentar_programa():
    print("INVESTING")


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


def obterUltimoId(investimentos):
    # pegar o ultimo Id
    ultimoInvestimento = investimentos[-1:]
    ultimoId = ultimoInvestimento[0]['id']
    # adicionar em seguida
    ultimoId += 1
    return ultimoId


def criarNovoInvestimento(nome, valor):
    # Saber quais são osinvestimentos existentes
    investimentos = lerInvestimentosExistentes()
    ultimoId = obterUltimoId(investimentos)
    novoInvestimento = {'id': ultimoId, 'nome': nome, 'valor': valor}
    investimentos.append(novoInvestimento)

    salvarAlteracoes(investimentos)


def salvarAlteracoes(investimentos):
    investimentoJson = json.dumps(investimentos)
    Path('investimentos.json').write_text(investimentoJson)


def editar_investimento_existente(investimento_id):
    investimentos = lerInvestimentosExistentes()
    nome = input("Qual o novo investimento: ")
    valor = input("Qual o valor do Investimento: ")
    for investimento in investimentos:
        if investimento['id'] == int(investimento_id):
            if nome != '':
                investimento.update({'nome': nome})
            if valor != '':
                investimento.update({'valor': int(valor)})
            salvarAlteracoes(investimentos)
            print(investimento)


def excluirInvestimento(investimento_id):
    investimentos = lerInvestimentosExistentes()
    for indice, item in enumerate(investimentos):
        if item['id'] == int(investimento_id):
            print(f"O investimento {item} foi excluído")
            del investimentos[indice]
            salvarAlteracoes(investimentos)
