import json
from flask import jsonify, request
from recursion import app
from recursion.schema import User, Role

teacherRole = Role(name="Teacher")
studentRole = Role(name="Student")


from flask import request

@app.route('/user/login', methods=['POST'])
def login_user():
    data = json.loads(request.data)
    user = User.objects(email=data['login']).first()
    if user is None:
        return jsonify({"error": "User not found"}), 404
    else:
        if user.password == data['password']:
            return jsonify(user), 200
        else:
            return jsonify({"error": "Incorrect password"}), 405

@app.route('/user/create', methods=['PUT'])
def create_user():
    """Create a new user."""
    data = json.loads(request.data)
    try:
        user = User(**data)
        user.save()
        return jsonify(user), 200

    except Exception as e:
        return jsonify({"error": e.__class__.__name__}), 405
        

@app.route('/user/update/<string:id>', methods=['PATCH'])
def update_user(id):
    """Update a user."""
    data = json.loads(request.data)
    user = User.objects(id=id).first()
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    for key, value in data.items():
        user[key] = value

    user.save()
    return jsonify(user), 200

@app.route('/user/delete/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = User.objects(id=id).first()
    if user is None:
        return jsonify({"error": "User not found" }), 404
    
    user.delete()
    return jsonify({"success": True}), 200

@app.route('/user/get', methods=['GET'])
def get_users():
    """Get a users."""
    data = User.objects.all()
    if data is None:
        return jsonify({"error": "Users not found"}), 404

    return jsonify(data), 200

@app.route('/user/get/<string:id>', methods=['GET'])
def get_user(id):
    """Get a user."""
    data = User.objects(id=id).first()
    if data is None:
        return jsonify({"error": "User not found" }), 404

    return jsonify(data), 200