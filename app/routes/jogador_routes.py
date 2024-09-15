from flask import Blueprint, render_template
from app.models import Jogador

jogador_bp = Blueprint('jogadores', __name__)

@jogador_bp.route('/')
def listar_jogadores():
    jogadores = Jogador.query.all()
    return render_template('jogadores/listar.html', jogadores=jogadores)

@jogador_bp.route('/<int:jogador_id>')
def detalhe_jogador(jogador_id):
    jogador = Jogador.query.get_or_404(jogador_id)
    return render_template('jogadores/detalhe.html', jogador=jogador)
