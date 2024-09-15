import pandas as pd

# Função para importar jogadores do CSV
def importar_jogadores_csv(caminho_csv):
    df = pd.read_csv(caminho_csv)
    return df

def tratar_df(df):
    df_clean = df.dropna(how='all')

    # Manter apenas as colunas até "Baralho"
    df_clean = df_clean.loc[:, :'Local']

    # Substituir valores errados como '#VALUE!' por NaN
    df_clean.replace('#VALUE!', pd.NA, inplace=True)

    # Opcional: Remover linhas onde a coluna 'Vencedores' tem NaN
    df_clean = df_clean.dropna(subset=['Vencedores'])

    df = df_clean

    # Substituir '#VALUE!' por NaN
    df.replace('#VALUE!', pd.NA, inplace=True)
    df.replace('Nan', pd.NA, inplace=True)
    df.replace('<NA>', pd.NA, inplace=True)

    df['Vencedores'] = df['Vencedores'].str.split(' e ')
    vencedores = df['Vencedores']
    vencedores.dropna(inplace=True)

    # Função para identificar os perdedores
    def get_perdedores(row):
        # Todos os jogadores
        jogadores = [row['Jogador 1'], row['Jogador 2'], row['Jogador 3'], row['Jogador 4']]
        
        # Filtrar quem não está na lista de vencedores
        perdedores = [jogador for jogador in jogadores if jogador not in row['Vencedores']]
        
        return perdedores

    # Criar a coluna 'Perdedores'
    df['Perdedores'] = df.apply(get_perdedores, axis=1)

    # Move column 
    col_to_move = 'Placar'
    new_position = 0

    # Get a list of columns excluding the one to move
    cols = [col for col in df.columns if col != col_to_move]

    # Insert 'B' at the desired position
    cols.insert(new_position, col_to_move)

    # Reorder the DataFrame columns
    df = df[cols]

    # Drop columns from 'Jogador 1' to 'Jogador 4'
    df = df.drop(df.loc[:, 'Jogador 1':'Jogador 4'].columns, axis=1)

    # Função para ordenar os números dentro de cada célula
    def ordenar_numeros(valor):
        numeros = list(map(int, valor.split('x')))
        return 'x'.join(map(str, sorted(numeros, reverse=True)))  # Ordena em ordem decrescente

    # Aplica a função à coluna desejada
    df['Placar'] = df['Placar'].apply(ordenar_numeros)

    # Move column 
    col_to_move = 'Placar'
    new_position = 2

    # Get a list of columns excluding the one to move
    cols = [col for col in df.columns if col != col_to_move]

    # Insert 'B' at the desired position
    cols.insert(new_position, col_to_move)

    # Reorder the DataFrame columns
    df = df[cols]

    # Move column 
    col_to_move = 'Local'
    new_position = 4

    # Get a list of columns excluding the one to move
    cols = [col for col in df.columns if col != col_to_move]

    # Insert 'B' at the desired position
    cols.insert(new_position, col_to_move)

    # Reorder the DataFrame columns
    df = df[cols]
    return df

def create_links_partidas(df):
    # Adicionando links para cada vencedor
    def create_links(column):
        links = [f'<a href="/jogador/{player}">{player}</a>' for player in column]
        return ', '.join(links)  # Separa os links com vírgulas

    df['Vencedores'] = df['Vencedores'].apply(create_links)
    df['Perdedores'] = df['Perdedores'].apply(create_links)


    return df


def create_links_jogador(df):
    # Adicionando links para cada vencedor
    def create_links(column):
        links = [f'<a href="/jogador/{player}">{player}</a>' for player in column]
        return ', '.join(links)  # Separa os links com vírgulas

    df['Dupla'] = df['Dupla'].apply(create_links)
    df['Oponente'] = df['Oponente'].apply(create_links)

    return df

# Função para criar o DataFrame de cada jogador com a informação da dupla
def criar_df_jogador(jogador, df):
    dados_jogador = {'Dia': [], 'Resultado': [], 'Dupla': [], 'Oponente': [], 'Placar': [], 'Local': []}
    
    for idx, row in df.iterrows():
        if jogador in row['Vencedores']:
            dupla = [comp for comp in row['Vencedores'] if comp != jogador]
            dados_jogador['Dia'].append(row['Dia'])
            dados_jogador['Resultado'].append('Vitória')
            dados_jogador['Dupla'].append(dupla)
            dados_jogador['Oponente'].append(row['Perdedores'])
            dados_jogador['Placar'].append(row['Placar'])
            dados_jogador['Local'].append(row['Local'])
        elif jogador in row['Perdedores']:
            dupla = [comp for comp in row['Perdedores'] if comp != jogador]
            dados_jogador['Dia'].append(row['Dia'])
            dados_jogador['Resultado'].append('Derrota')
            dados_jogador['Dupla'].append(dupla)
            dados_jogador['Oponente'].append(row['Vencedores'])
            dados_jogador['Placar'].append(row['Placar'])
            dados_jogador['Local'].append(row['Local'])
    
    df_jogador = pd.DataFrame(dados_jogador)
    return df_jogador
