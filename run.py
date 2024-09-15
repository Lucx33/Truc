from app import create_app, db
from app.models import Jogador
import pandas as pd

# Função para importar jogadores do CSV
def importar_jogadores_csv(caminho_csv):
    df = pd.read_csv(caminho_csv)
        
    # Verifica se o banco já está populado
    if Jogador.query.count() == 0:  # Evita duplicação de dados
        for index, row in df.iterrows():
            jogador = Jogador(
                id=row['id'],
                nome=row['nome'],
                vitorias=row['vitórias'],
                derrotas=row['derrotas'],
                saldo=row['saldo']
            )
            db.session.add(jogador)
        db.session.commit()

# Cria o app
app = create_app()

# Verifica se o banco já está inicializado e faz a importação
with app.app_context():
    importar_jogadores_csv('Log Truco - Serie A 2024.2 - Página1.csv')

if __name__ == "__main__":
    app.run(debug=True)
