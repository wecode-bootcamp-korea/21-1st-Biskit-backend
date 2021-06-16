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
            account       = data['account']
            account_Regex = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{6,20}$)'

            if not re.match (account_Regex, account):
                  return JsonResponse({'message':'INVALID_FORMAT'}, status=400)             
            if User.objects.filter(account = account).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)
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
            
            account_Regex   = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{6,20}$)'
            password_Regex  = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^~@$!%*#?&])[A-Za-z\d^~@$!#%*?&]{8,20}$'
            mobile_Regex    = '^[0-9]{3}[0-9]{4}[0-9]{4}$'
            email_Regex     = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
            name_Regex      = '^[가-힣]+'
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if ('' == account) or ('' == password):
                return JsonResponse({'message':'VALUE_IS_EMPTY'}, status=400)
<<<<<<< HEAD
            # if not re.match (account_Regex, account) or (name_Regex, name) or (email_Regex, email) or (password_Regex, password) or (mobile_Regex, mobile):
            #     return JsonResponse({'message':'INVALID_FORMAT'}, status=400)   
=======
            if not re.match(account_Regex, account) or\
               not re.match(password_Regex, password) or\
               not re.match(mobile_Regex, mobile) or\
               not re.match(name_Regex, name) or\
               not re.match(email_Regex, email):
                return JsonResponse({'message':'INVALID_FORMAT'}, status=400)
>>>>>>> main
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
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            account  = data['account']
            password = data['password']
            user     = User.objects.get(account=account)

            if not User.objects.filter(account=data['account']).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=400)
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'WRONG_PASSWORD'}, status= 400)
            token = jwt.encode({'user_id':user.id}, SECRET_KEY, ALGORITHM)
            return JsonResponse({'token':token, 'message':'SUCCESS'}, status=200)
        except KeyError: 
            return JsonResponse ({'message':'KEY_ERROR'}, status=400) 
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)