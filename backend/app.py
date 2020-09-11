from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, current_identity
from resources.user import UserRegister
from resources.question import Question, QuestionList
from resources.option import Option
from resources.quiz import Quiz, QuizList
from security import authenticate, identity
from db import db

app = Flask(__name__)
app.secret_key = 'jose'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)

db.init_app(app)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Option, '/question/option/<int:_id>')
api.add_resource(QuestionList, '/<int:_id>/questions')
api.add_resource(UserRegister, '/register')
api.add_resource(QuizList , '/quizzes')
api.add_resource(Quiz, '/quiz/<int:_id>')
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True