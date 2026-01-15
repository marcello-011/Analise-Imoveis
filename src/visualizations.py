import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# VISUALIZAÇÃO 1 — Tipo de imóvel (cidade toda)
# ==================================================
def plot_tipo_imovel(resultado):
    """
    Plota o valor médio do aluguel por m²
    por tipo de imóvel.
    """
    plt.figure(figsize=(6, 4))
    resultado.plot(kind='barh')
    plt.title('Valor médio do aluguel por m² por tipo de imóvel')
    plt.xlabel('R$ / m²')
    plt.ylabel('Tipo de imóvel')
    plt.tight_layout()
    plt.show()


# ==================================================
# VISUALIZAÇÃO 2 — Tipo de imóvel dentro de um bairro
# ==================================================
def plot_bairro_tipo(dados_bairro, bairro):
    """
    Plota o valor médio do aluguel por m²
    por tipo de imóvel dentro de um bairro específico.
    """
    if dados_bairro is None or dados_bairro.empty:
        print(f'Não há dados suficientes para o bairro "{bairro}".')
        return

    plt.figure(figsize=(6, 4))
    plt.bar(dados_bairro['type'], dados_bairro['valor_m2'])
    plt.title(f'Aluguel médio por m² por tipo – {bairro}')
    plt.ylabel('R$ / m²')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


# ==================================================
# VISUALIZAÇÃO 3 — Heatmap Bairro × Tipo
# ==================================================
def plot_heatmap(tabela):
    """
    Plota um heatmap do valor médio do aluguel por m²
    cruzando bairro e tipo de imóvel.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(tabela, cmap='viridis')
    plt.title('Aluguel médio por m² — Bairro × Tipo de imóvel')
    plt.xlabel('Tipo de imóvel')
    plt.ylabel('Bairro')
    plt.tight_layout()
    plt.show()
