from flask import Blueprint, render_template
from app.models import Dupla

dupla_bp = Blueprint('duplas', __name__)

@dupla_bp.route('/')
def listar_duplas():
    duplas = Dupla.query.all()
    return render_template('duplas/listar.html', duplas=duplas)

@dupla_bp.route('/<int:dupla_id>')
def detalhe_dupla(dupla_id):
    dupla = Dupla.query.get_or_404(dupla_id)
    return render_template('duplas/detalhe.html', dupla=dupla)
    