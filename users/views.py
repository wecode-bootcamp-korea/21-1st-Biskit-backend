import json
import re
import jwt
import bcrypt

from django.views     import View
from django.http      import JsonResponse

from .models          import User
from biskit_settings  import SECRET_KEY,ALGORITHM

class AccountCheckView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            account  = data['account']

            if User.objects.filter(account = account).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)
            else: 
                return JsonResponse({'message':'SUCCESS'}, status=200) 
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)


class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            name     = data['name']
            account  = data['account']
            mobile   = data['mobile']
            address  = data['address']
            email    = data['email']
            password = data['password']
            
            account_Regex   = '(?!.*[\.\-\_]{2,})^[a-zA-Z0-9\.\-\_]{6,20}$'
            password_Regex  = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,12}$'
            email_Regex     = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            mobile_Regex    = '\d{3,4}-\d{4}'
            name_Regex      = '[가-힣]'
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if ('' == account) or ('' == password):
                return JsonResponse({'message':'VALUE_IS_EMPTY'}, status=400)
            if not re.match (account_Regex, account) or (name_Regex, name) or (email_Regex, email) or (password_Regex, password) or (mobile_Regex, mobile):
                return JsonResponse({'message':'INVALID_FORMAT'}, status=400)   
            if User.objects.filter(account = account).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)

            User.objects.create(
                name     = name,
                account  = account,
                password = hashed_password,
                mobile   = mobile, 
                address  = address,
                email    = email 
            ) 
            return JsonResponse({'message':'SUCCESS'}, status= 201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            account     = data['account']
            password    = data['password']
            user        = User.objects.get(account=account)
          
            if not User.objects.filter(account=data['account']).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'WRONG_PASSWORD'}, status= 200)
            token = jwt.encode({'user_id':user.id}, SECRET_KEY, ALGORITHM)
            return JsonResponse({'token':token}, status=200)
        except KeyError: 
            return JsonResponse ({'message':'KEY_ERROR'}, status=400) 
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)   
        