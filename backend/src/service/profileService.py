from ..models import profileModel

def get_profile(user_id):
    return profileModel.getProfile(user_id)
