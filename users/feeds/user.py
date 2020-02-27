import uuid, random
from django.http import HttpResponseNotAllowed


class UserRepository:

    def __init__(self, **kwargs):
        self.user = kwargs['user']

    def change_token(self):

        user = self.user
        if user.is_authenticated:
            new_token = uuid.uuid4()
            user.jwt_secret = new_token
            user.save()
        else:
            raise HttpResponseNotAllowed

        return new_token

    def user_role_company_id(self):
        pass


def create_activate_token():

    number = random.randrange(100000, 999999, 1)

    return number


def jwt_response_payload_handler(token, user=None, request=None):
    from users.serializers.user import UserSerializer

    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.
    """
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
