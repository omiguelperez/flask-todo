"""Firestore service."""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_user(user_id):
    """Return user from firestore by username."""
    return db.collection('users').document(user_id).get()


def get_users():
    """Return users from firestore."""
    return db.collection('users').get()


def user_put(user_data):
    """Create an user on database."""
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_todos(username):
    """Get todos filtered by username."""
    return db.collection('users').document(username).collection('todos').get()


def put_todo(username, description):
    """Create todo on database."""
    todo_collection_ref = db.collection('users').document(username).collection('todos')
    todo_collection_ref.add({'description': description, 'done': False})


def delete_todo(username, todo_id):
    """Remove todo from database."""
    todo_ref = _get_todo_ref(username, todo_id)
    todo_ref.delete()


def _get_todo_ref(username, todo_id):
    """Return todo reference."""
    return db.collection('users').document(username).collection('todos').document(todo_id)
