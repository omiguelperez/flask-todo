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


def get_todos(username):
    """Get todos filtered by username."""
    return db.collection('users').document(username).collection('todos').get()
