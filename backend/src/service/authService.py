from ..models import authModel

def find_user(username):
    return authModel.findUserByUsername(username)


def authenticate_user(username, password):
    return authModel.authenticateUser(username, password)


def change_password(username, old_password, new_password):
    user = authModel.authenticateUser(username, old_password)
    if not user:
        return None
    return authModel.updatePassword(username, new_password)
