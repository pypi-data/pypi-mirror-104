from apiflask import APIFlask, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask.views import MethodView

app = APIFlask(__name__)

pets = [
    {
        'id': 0,
        'name': 'Kitty',
        'category': 'cat'
    },
    {
        'id': "100",
        'name': 'Coco',
        'category': 'dog'
    },
    {
        'id': 2,
        'name': 'Flash',
        'category': 'cat'
    }
]


class PetInSchema(Schema):
    name = String(required=True, validate=Length(0, 10))
    category = String(required=True, validate=OneOf(['dog', 'cat']))


class PetOutSchema(Schema):
    id = Integer()
    name = String()
    category = String()


@app.route('/')
class Hello(MethodView):

    def get(self):
        return {'message': 'Hello!'}


@app.route('/pets/<int:pet_id>')
class Pet(MethodView):

    @output(PetOutSchema)
    def get(self, pet_id):
        if pet_id > len(pets) - 1:
            abort(404)
        return pets[pet_id]

    @input(PetInSchema)
    @output(PetOutSchema)
    def put(self, pet_id, data):
        if pet_id > len(pets) - 1:
            abort(404)
        data['id'] = pet_id
        pets[pet_id] = data
        return pets[pet_id]

    @input(PetInSchema(partial=True))
    @output(PetOutSchema)
    def patch(self, pet_id, data):
        if pet_id > len(pets) - 1:
            abort(404)
        for attr, value in data.items():
            pets[pet_id][attr] = value
        return pets[pet_id]

    @output({}, 204)
    def delete(self, pet_id):
        if pet_id > len(pets) - 1:
            abort(404)
        pets.pop(pet_id)
        return ''


@app.route('/pets')
class Pets(MethodView):

    @output(PetOutSchema(many=True))
    def get(self):
        return pets

    @input(PetInSchema)
    @output(PetOutSchema, 201)
    def post(self, data):
        pet_id = len(pets)
        data['id'] = pet_id
        pets.append(data)
        return pets[pet_id]
