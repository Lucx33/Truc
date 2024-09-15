from . import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    partidas_vencidas = db.Column(db.Integer, default=0)
    partidas_perdidas = db.Column(db.Integer, default=0)
    saldo = db.Column(db.Integer, default=0)
    dupla_id = db.Column(db.Integer, db.ForeignKey('dupla.id'), nullable=True)
    dupla = db.relationship('Dupla', back_populates='jogadores')

class Dupla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    partidas_vencidas = db.Column(db.Integer, default=0)
    partidas_perdidas = db.Column(db.Integer, default=0)
    saldo = db.Column(db.Integer, default=0)
    jogadores = db.relationship('Jogador', back_populates='dupla')
