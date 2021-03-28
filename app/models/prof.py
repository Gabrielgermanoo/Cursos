from app import db

class Professor(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    nome = db.Column(db.String(64), index = True)
    data_nascimento = db.Column(db.Date, index = True)
    formacao = db.Column(db.String(64), index = True)
    

    def __repr__(self):
        return '<Professor {} ({})'. format(self.nome, self.data_nascimento, self.formacao)