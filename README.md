# Analise-Imoveis

Este projeto foi desenvolvido em Python com o objetivo de facilitar a análise exploratória de dados imobiliários, resolvendo um problema comum encontrado por analistas, estudantes e profissionais da área: a dificuldade de identificar padrões claros de distribuição de imóveis por tipo e localização a partir de dados brutos.

Na prática, bases de dados imobiliárias costumam ser grandes, pouco intuitivas e difíceis de interpretar apenas olhando tabelas. Informações como tipo de imóvel, distrito e quantidade ficam dispersas, o que torna a tomada de decisão mais lenta e sujeita a erros.

Pensando nisso, este projeto foi criado para transformar dados brutos em informações visuais e organizadas, permitindo:

entender rapidamente quais tipos de imóveis são mais comuns no conjunto de dados

comparar a distribuição de tipos de imóveis entre diferentes distritos

identificar padrões globais de concentração por meio de visualizações (heatmap)

reduzir erros de digitação e interpretação ao disponibilizar uma lista de distritos existentes no dataset

O sistema funciona através de um menu interativo em terminal, onde o usuário pode escolher diferentes análises sem precisar escrever código, tornando a ferramenta acessível mesmo para quem não tem familiaridade com programação avançada.

Além disso, o projeto foi estruturado seguindo boas práticas de organização, separando claramente:

carregamento e preparação dos dados

regras de negócio e análises

visualizações gráficas

controle de fluxo e interação com o usuário

Isso torna o código fácil de manter, expandir e evoluir, sendo um ótimo ponto de partida para projetos maiores na área de Data Science e Análise de Dados.

🚀 Funcionalidades

Visão geral da distribuição de imóveis por tipo

Análise detalhada de tipos de imóveis dentro de um distrito específico

Visualização global dos padrões usando heatmap (distrito × tipo de imóvel)

Listagem de todos os distritos disponíveis no dataset para facilitar pesquisas precisas

🛠️ Tecnologias Utilizadas

Python 3.9.9

Pandas — manipulação e análise de dados

Matplotlib / Seaborn — visualização gráfica

Este projeto foi desenvolvido com foco educacional e prático, simulando um cenário real de análise exploratória de dados, e pode ser facilmente adaptado para outros conjuntos de dados ou expandido com novas análises.

![Heatmap de aluguel por distrito e tipo](docs/heatmap_bairro_tipo.png)
