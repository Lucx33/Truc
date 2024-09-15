from app import create_app
import pandas as pd


# Função para importar jogadores do CSV
def importar_jogadores_csv(caminho_csv):
    df = pd.read_csv(caminho_csv)
        

# Cria o app
app = create_app()

# Verifica se o banco já está inicializado e faz a importação
with app.app_context():
    importar_jogadores_csv('Log Truco - Serie A 2024.2 - Página1.csv')

if __name__ == "__main__":
    app.run(debug=True)
