from flask import Blueprint, render_template
import pandas as pd
import app.utils as utils

main = Blueprint('main', __name__)

# Importar e tratar o DataFrame
df = utils.importar_jogadores_csv('Log Truco - Serie A 2024.2 - 16-09.csv')
df = utils.tratar_df(df)

# Coletando todos os jogadores únicos
jogadores = set([jogador for sublist in df['Vencedores'] + df['Perdedores'] for jogador in sublist])

# Criando um DataFrame individual para cada jogador
jogador_dfs = {jogador: utils.criar_df_jogador(jogador, df) for jogador in jogadores}

# Calculando as estatísticas de winrate para cada jogador
jogador_stats = {jogador: utils.calcular_winrate(jogador_dfs[jogador]) for jogador in jogadores}

# Criando links HTML para as partidas
df_html = utils.create_links_partidas(df)
df_jogador_html = {jogador: utils.create_links_jogador(df_jogador) for jogador, df_jogador in jogador_dfs.items()}

@main.route('/')
def show_dataframe():
    # Convertendo o DataFrame para HTML
    df_html = df.to_html(classes='table table-striped', index=False, escape=False)  # escape=False permite tags HTML
    
    return render_template('tabela.html', table=df_html)

# Rota para exibir detalhes do jogador
@main.route('/jogador/<nome>')
def jogador_perfil(nome):
    # Obter o DataFrame do jogador selecionado
    df_jogador = jogador_dfs.get(nome)
    stats = jogador_stats.get(nome)

    if df_jogador is not None and stats is not None:
        df_jogador_html = df_jogador.to_html(classes='table table-striped', index=False, escape=False)
        return render_template('perfil.html', table=df_jogador_html, stats=stats)
    else:
        return f"Jogador {nome} não encontrado.", 404
