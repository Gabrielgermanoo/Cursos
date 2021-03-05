from app import db

class Curso(db.Model):
    __tablename__ = "curso"

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(64), index=True)
    tipo = db.Column(db.String(64), index=True)
    duracao = db.Column(db.Float(), index=True)
    avaliacoes = db.relationship('Avaliacao', backref='nome', lazy='dynamic')

    def __repr__(self):
        return '<Curso {} ({})>' .format(self.nome, self.tipo)