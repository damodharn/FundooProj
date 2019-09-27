from functools import wraps
import jwt
from .services import Redis
from django.conf import settings
from .models import User


def login_require(func):
    @wraps
    def wrapper_fun(*args, **kwargs):
        username = args[0].POST.get['username']
        print(username)
        redis_object = Redis()
        jwt_token = redis_object.get(username)
        decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY)
        user_id = decoded_token['id']
        id = User.objects.values('id')
        for i in range(len(id)):
            if (id[i]['id']) == user_id:  # getting the user id from the query set
                return func(*args, **kwargs)
            else:
                continue
    return wrapper_fun
