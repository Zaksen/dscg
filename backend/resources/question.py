from flask_restful import Resource, reqparse
from models.question import QuestionModel
from models.quiz import QuizModel

class Question(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('label',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('quiz_id',
        type=int,
        required=True,
        help="Every question needs a quiz id"
    )
    
    def get(self, _id):
        question = QuestionModel.find_by_id(_id)
        if question:
            return question.json()
        return {'message' : 'Question not found'}, 404

    def post(self):
        data = Question.parser.parse_args()
        question = QuestionModel(**data)
        try:
            question.save_to_db()
        except:
            return {'message' : 'internal error'}, 500

        return question.json(), 201


    def delete(self, name):
        question = QuestionModel.find_by_name(name)
        if question:
            question.delete_from_db()
        
        return {'message' : 'Question deleted'}

class QuestionList(Resource):
    def get(self):
        return {'Questions' : [question.json() for question in QuestionModel.query.all()]}
        
class QuizQuestions(Resource):
    def get(self, _id):
        quiz = QuizModel.find_by_id(_id).json()
        if quiz:
            return {'Questions' : quiz['questions']}, 201
        return {'message' : 'Question not found'}, 404