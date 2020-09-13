from db import db

class QuizModel(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    theme = db.Column(db.String(80))

    questions = db.relationship('QuestionModel', lazy='dynamic')

    def __init__(self, name, theme):
        self.name = name
        self.theme = theme

    def json(self):
        return {'id':self.id, 'name':self.name, 'questions':[question.json() for question in self.questions.all()], 'theme':self.theme}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()