from db import db

class OptionModel(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80), nullable=False)
    is_right = db.Column(db.Boolean, nullable=False)
    
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('QuestionModel')

    def __init__(self, label, question_id, is_right):
        self.label = label
        self.question_id = question_id
        self.is_right = is_right

    def json(self):
        return {'label':self.name, 'question_id': self.question_id}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()