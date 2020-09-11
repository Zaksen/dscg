from db import db

class QuestionModel(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(200))
    
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    quiz = db.relationship('QuizModel')

    options = db.relationship('OptionModel', lazy='dynamic')

    def __init__(self, label, quiz_id):
        self.label = label
        self.quiz_id = quiz_id

    def json(self):
        return {'label':self.label, 'options':[option.json() for option in self.options.all()]}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()