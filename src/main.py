from data_loader import preparar_dados
from analyses import (
    analise_tipo_imovel,
    analise_bairro_tipo,
    analise_bairro_tipo_matriz,
    acao_listar_bairros
)
from visualizations import (
    plot_tipo_imovel,
    plot_bairro_tipo,
    plot_heatmap
)



# ==================================================
# Função principal
# ==================================================
def main():

    dados = preparar_dados('data/data.csv')

    while True:
        print("\n📊 Análises disponíveis:")
        print("1 - Tipo de imóvel (visão geral)")
        print("2 - Tipo de imóvel dentro de um bairro")
        print("3 - Padrão global (heatmap bairro × tipo)")
        print("4 - Listar bairros disponíveis")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            resultado = analise_tipo_imovel(dados)
            plot_tipo_imovel(resultado)

        elif opcao == "2":
            bairro = input("Digite o nome do bairro: ").strip()
            resultado = analise_bairro_tipo(dados, bairro)

            if resultado is None:
                print("❌ Bairro não encontrado ou sem dados suficientes.")
            else:
                plot_bairro_tipo(resultado, bairro)

        elif opcao == "3":
            tabela = analise_bairro_tipo_matriz(dados)
            plot_heatmap(tabela)

        elif opcao == "4":
            acao_listar_bairros(dados)

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("❌ Opção inválida.")




# ==================================================
# Ponto de entrada
# ==================================================
if __name__ == "__main__":
    main()
