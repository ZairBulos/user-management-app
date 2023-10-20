from flask import Blueprint, jsonify, request
from src.models.User import User

main = Blueprint('user_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = [user.to_JSON() for user in User.query.all()]
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/<id>')
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user is None:
            return jsonify({'error': 'user not found'}), 404

        return jsonify(user.to_JSON())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/', methods=['POST'])
def save_user():
    try:
        name = request.json['name']
        last_name = request.json['lastName']
        age = request.json['age']

        user = User.create(name, last_name, age)
        return jsonify(user.to_JSON())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/<id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user is None:
            return jsonify({'error': 'user not found'}), 404

        user.name = request.json['name']
        user.last_name = request.json['lastName']
        user.age = request.json['age']

        user.update()
        return jsonify(user.to_JSON())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user is None:
            return jsonify({'error': 'user not found'}), 404

        user.delete()
        return jsonify({})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
