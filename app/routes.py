from flask import Blueprint, render_template
import pandas as pd
import app.utils as utils


main = Blueprint('main', __name__)

df = utils.importar_jogadores_csv('Log Truco - Serie A 2024.2 - Página1.csv')
df = utils.tratar_df(df)

jogadores = set([jogador for sublist in df['Vencedores'] + df['Perdedores'] for jogador in sublist])

# Criando um DataFrame individual para cada jogador
jogador = {jogador: utils.criar_df_jogador(jogador, df) for jogador in jogadores}

df_html = utils.create_links_partidas(df)
df_jogador_html = {jogador: utils.create_links_jogador(df) for jogador, df in jogador.items()}

@main.route('/')
def show_dataframe():

    # Convertendo o DataFrame para HTML
    df_html = df.to_html(classes='table table-striped', index=False, escape=False)  # escape=False permite tags HTML
    
    # Convertendo o DataFrame para HTML
    df_html = df.to_html(classes='table table-striped', index=False, escape=False)  # escape=False permite tags HTML
    
    return render_template('dataframe.html', table=df_html)

# Rota para exibir detalhes do jogador
@main.route('/jogador/<nome>')
def jogador_perfil(nome):
    df_jogador = jogador[f"{nome}"]
    df_jogador_html = df_jogador.to_html(classes='table table-striped', index=False, escape=False)

    return render_template('dataframe.html', table=df_jogador_html)