"""Todo models."""

from flask_login import UserMixin

from app.firestore_service import get_user


class UserData:
    """User data."""

    def __init__(self, username, password):
        """Set to self user obj the required data."""
        self.username = username
        self.password = password


class UserModel(UserMixin):
    """User model."""

    def __init__(self, user_data):
        """Self model attrs from user data."""
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        """Get user from db."""
        user = get_user(username)
        user_data = UserData(
            username=user.id,
            password=user.to_dict()['password']
        )
        return UserModel(user_data)
