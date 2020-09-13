from flask_restful import Resource, reqparse
from models.quiz import QuizModel

class Quiz(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('theme',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    def get(self, _id):
        quiz = QuizModel.find_by_id(_id)
        if quiz:
            return quiz.json()
        return {'message' : 'Quiz not found'}, 404

class QuizList(Resource):
    def get(self):
        return {'Quizzes' : [quiz.json() for quiz in QuizModel.query.all()]}

class QuizPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('theme',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = QuizPost.parser.parse_args()
        quiz = QuizModel.find_by_name(data['name'])
        if quiz:
            return {'message':'Quiz with name already exists'}, 200
        else:
            quiz = QuizModel(**data)
            try:
                quiz.save_to_db()
            except:
                return {'message' : 'internal error'}, 500

        return quiz.json(), 201 