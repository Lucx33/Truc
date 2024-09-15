from app import create_app
from app.utils.importar_jogadores import importar_jogadores_csv

# Cria o app
app = create_app()

# Importa os jogadores do CSV
with app.app_context():
    importar_jogadores_csv('Log Truco - Serie A 2024.2 - Página1.csv')

if __name__ == "__main__":
    app.run(debug=True)
