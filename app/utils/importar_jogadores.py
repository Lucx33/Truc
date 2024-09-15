import pandas as pd

# Função para importar jogadores do CSV
def importar_jogadores_csv(caminho_csv):
    df = pd.read_csv(caminho_csv)
    # Lógica para manipular os dados do DataFrame
    print(df.head())  # Exemplo para exibir os dados importados
