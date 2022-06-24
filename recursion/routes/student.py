import json
from flask import jsonify, request
from recursion import app
from recursion.schema import Role, Student

@app.route('/student/create', methods=['PUT'])
def create_student():
    data = json.loads(request.data)
    try:
        student = Student(role=Role(name="student"), **data)
        print(student)
        student.save()
        return jsonify(student), 200

    except Exception as e:
        return jsonify({"error": e.__class__.__name__}), 500

@app.route('/student/get', methods=['GET'])
def get_students():
    data = Student.objects().all()
    return jsonify(data), 200

@app.route('/student/update', methods=['PATCH'])
def update_student():
    data = json.loads(request.data)
    try:
        student = Student.objects(email=data['email']).first()
        student.update(**data)
        return jsonify(student), 200

    except Exception as e:
        return jsonify(
            dict(message="Error", error=str(e))
        ), 500
        

# @app.route('/user/update/<string:id>', methods=['PATCH'])
# def update(id):
#     """Update a user."""
#     data = json.loads(request.data)
#     print(id)
#     print(data)
#     user = User.objects(id=id).first()
#     if user is None:
#         return jsonify({"error": "User not found"}), 404
    
#     for key, value in data.items():
#         user[key] = value

#     user.save()
#     return jsonify(user), 200

# @app.route('/user/delete/<string:id>', methods=['DELETE'])
# def delete(id):
#     user = User.objects(id=id).first()
#     print(id)
#     if user is None:
#         return jsonify({"error": "User not found" }), 404
    
#     user.delete()
#     return jsonify({"success": True}), 200

# @app.route('/user/get', methods=['GET'])
# def get_all():
#     """Get a users."""
#     data = User.objects.all()
#     if data is None:
#         return jsonify({"error": "Users not found"}), 404

#     return jsonify(data), 200

# @app.route('/user/get/<string:id>', methods=['GET'])
# def get_one(id):
#     """Get a user."""
#     data = User.objects(id=id).first()
#     if data is None:
#         return jsonify({"error": "User not found" }), 404

#     return jsonify(data), 200