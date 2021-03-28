from app import db


cursos_professores = db.Table('cursos_prof', 
    db.Column('curso_id', db.Integer, 
        db.ForeignKey('curso.id'), primary_key=True),
    db.Column('professor_id', db.Integer,
        db.ForeignKey('professor.id'), primary_key=True)
)

class Curso(db.Model):
    __tablename__ = "curso"

    id = db.Column(db.Integer(), primary_key=True)
    curso = db.Column(db.String(64), index=True)
    tipo = db.Column(db.String(64), index=True)
    duracao = db.Column(db.Integer(), index=True)
    avaliacoes = db.relationship('Avaliacao', backref='nome', lazy='dynamic')
    cursos_prof =  db.relationship('Professor', secondary= cursos_professores,
        backref=db.backref('cursos', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Curso {} ({})>' .format(self.curso, self.tipo)
