from utilidades import *


if __name__ == '__main__':
    apresentar_programa()
    exibirInvestimentoTotal()
    listarInvestimentos()

    while True:
        opcao = mostrarMenu()
        if opcao == 1:
            nome = input("Qual o novo investimento: ")
            valor = int(input("Qual o valor: "))
            criarNovoInvestimento(nome, valor)
        elif opcao == 2:
            listarInvestimentos(exibirTodos=True)
        elif opcao == 3:
            investimento_id = input("Qual investimento quer alterar: ")
            editar_investimento_existente(investimento_id)
        elif opcao == 4:
            investimento_id = input("Qual investimento quer excluir: ")
            opcao = input("Tem certeza que quer excluir: S/N: ").upper()
            if opcao == 'S':
                excluirInvestimento(investimento_id)
                listarInvestimentos()
            else:
                listarInvestimentos()
                opcao = mostrarMenu()
        elif opcao == 5:
            break
        else:
            print("Opção não disponível!")
            break
