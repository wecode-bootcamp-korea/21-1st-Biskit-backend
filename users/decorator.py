import jwt

from django.http import JsonResponse

from biskit_settings import SECRET_KEY,ALGORITHM
from .models         import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):    
        try:
            token        = request.headers.get('Authorization', None)
            token_data   = jwt.decode(token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id=token_data['user_id'])
            request.user = user

            if token is None : 
                return JsonResponse({'message':'INVALID_USER'}, status=400)
        except jwt.DecodeError:
            return JsonResponse({'message':'DECODE_ERROR'}, status=400)
        except jwt.InvalidTokenError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status = 400)
        return func(self, request, *args, **kwargs)
    return wrapper