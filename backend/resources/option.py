from flask_restful import Resource, reqparse
from models.option import OptionModel

class Option(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('label',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('question_id',
        type=int,
        required=True,
        help="Every option need a question"
    )

    def get(self, _id):
        option = OptionModel.find_by_id(_id)
        if option:
            return option.json()
        return {'message' : 'Item not found'}, 404

    def post(self):
        data = Option.parser.parse_args()
        option = OptionModel(**data)
        try:
            option.save_to_db()
        except:
            return {"message":"an error occured"}, 500

        return option.json(), 201

    def delete(self, _id):
        option = OptionModel.find_by_id(_id)
        if option:
            option.delete_from_db()
        return {'message': 'item deleted'}, 201
