#!/usr/bin/python3
"""to get all states and uodate a new one if any"""

from flask import abort, jsonify, request
from models.state import State
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """to reyreive all the states created and updated"""
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """state object will be retreived from here"""
    state = storage.get(State, state_id)
    if state:
        
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """to delete the un needed objects"""
    state = storage.get(State, state_id)
    if stata:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """create objects for state"""
    if not request.get_json():
        abort(400, 'Not a JSON')


    kwargs = request.get_json()
    if 'name' not in kwargs:
        abort(400, 'Missing name')


    state = State(**kwargs)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """updates the existing ibjects"""
    state = storage.get(State, state_id)
    if state:
        if not request.get_json():
            abort(400, 'Not a JSON')


        data = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(state, key, value)

        state.save
        return jsonify(state.to_dict()), 200
    else:
        abort(404)


@app_views.errorhandler(404)
def not_found(error):
    """not found erro in java """
    
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app_views.errorhandler(400)
def bad_request(error):
    """a 404 erereror for bad request"""
    response = {'error': 'Bad Request'}
    return jsonify(response), 400
