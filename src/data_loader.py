import pandas as pd

def preparar_dados(caminho_csv, minimo_imoveis=50):
    """
    Carrega os dados de imóveis, filtra bairros com baixa
    representatividade e cria a coluna de valor por m².
    """
    imoveis = pd.read_csv(caminho_csv)

    # Contar quantidade de imóveis por bairro
    contagem_bairros = imoveis['district'].value_counts()

    # Selecionar bairros com >= minimo_imoveis
    bairros_validos = contagem_bairros[contagem_bairros >= minimo_imoveis].index

    # Filtrar dataset
    imoveis_filtrados = imoveis[imoveis['district'].isin(bairros_validos)].copy()

    # Criar métrica principal
    imoveis_filtrados['valor_m2'] = imoveis_filtrados['total'] / imoveis_filtrados['area']

    return imoveis_filtrados


