from app import db
from datetime import datetime


class Avaliacao(db.Model):
    __tablename__ = "avaliacoes"
    
    id = db.Column(db.Integer, primary_key=True)
    estrelas = db.Column(db.Integer(), index=True)
    timestamp = db.Column(db.DateTime, index=True, default =datetime.utcnow)
    curso_id = db.Column(db.Integer(), db.ForeignKey('nome.id'))

    def __repr__(self):
        return '<Avaliacao {}>'.format(self.estrelas)