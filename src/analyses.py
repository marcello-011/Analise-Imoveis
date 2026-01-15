import pandas as pd

# ==================================================
# ANÁLISE 1 — Tipo de imóvel (cidade toda)
# ==================================================
def analise_tipo_imovel(imoveis_filtrados):
    """
    Retorna o valor médio do aluguel por m²
    para cada tipo de imóvel.
    """
    resultado = (
        imoveis_filtrados
            .groupby('type')['valor_m2']
            .mean()
            .sort_values()
    )
    return resultado


def acao_listar_bairros(dados):
    """
    Lista todos os bairros disponíveis no dataset
    """
    # Ajuste o nome da coluna se necessário
    coluna_bairro = "district"

    bairros = (
        dados[coluna_bairro]
        .dropna()          # remove valores nulos
        .unique()          # remove duplicados
    )

    bairros_ordenados = sorted(bairros)

    print("\n🏙️ Bairros disponíveis:")
    for bairro in bairros_ordenados:
        print(f"- {bairro}")



# ==================================================
# ANÁLISE 2 — Tipo de imóvel dentro de um bairro
# ==================================================
def analise_bairro_tipo(imoveis_filtrados, bairro):
    """
    Retorna o valor médio do aluguel por m²
    por tipo de imóvel dentro de um bairro específico.
    """
    resultado = (
        imoveis_filtrados
            .groupby(['district', 'type'])['valor_m2']
            .mean()
            .reset_index()
    )

    dados_bairro = resultado[resultado['district'] == bairro]

    if dados_bairro.empty:
        return None

    return dados_bairro.sort_values('valor_m2', ascending=False)


# ==================================================
# ANÁLISE 3 — Matriz Bairro × Tipo
# ==================================================
def analise_bairro_tipo_matriz(imoveis_filtrados):
    """
    Retorna uma matriz (DataFrame) com o valor médio
    do aluguel por m² cruzando bairro e tipo de imóvel.
    """
    tabela = (
        imoveis_filtrados
            .groupby(['district', 'type'])['valor_m2']
            .mean()
            .unstack()
    )
    return tabela
