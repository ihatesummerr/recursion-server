import json
from flask import jsonify, request
from recursion import app
from recursion.schema import Event, User


from flask import request


@app.route('/event/create', methods=['PUT'])
def create_event():
    """Create a new event."""
    data = json.loads(request.data)
    try:
        event = Event(**data)
        event.save()
        return jsonify(event), 200

    except Exception as e:
        return jsonify({"error": e.__class__.__name__}), 405

@app.route('/event/get', methods=['GET'])
def get_events():
    data = Event.objects.all()
    if data is None:
        return jsonify({"error": "Events not found"}), 404

    return jsonify(data), 200

@app.route('/event/get', methods=['POST'])
def get_events_by_user():
    data = json.loads(request.data)
    user = User.objects(email=data['email']).first()

@app.route('/event/update', methods=['PATCH'])
def update_event():
    """Update a event."""
    data = json.loads(request.data)
    event = Event.objects(event_id=data['event_id']).first()
    if event is None:
        return jsonify({"error": "event not found"}), 404
    
    event.update(**data)

    event.save()
    return jsonify(event), 200

@app.route('/event/delete/', methods=['DELETE'])
def delete_event():
    data = json.loads(request.data)
    event = Event.objects(event_id=data['event_id']).first()

    if event is None:
        return jsonify({"error": "event not found"}), 404

    id = event.event_id
    event.delete()
    return jsonify(id), 200