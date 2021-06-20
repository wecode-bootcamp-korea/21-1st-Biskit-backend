import json, re, jwt, bcrypt

from django.views     import View
from django.http      import JsonResponse

from .models          import User
from biskit_settings  import SECRET_KEY,ALGORITHM

class AccountCheckView(View):
    def post(self,request):
        try:
            data          = json.loads(request.body)
            account       = data['account']
            ACCOUNT_REGEX = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{6,20}$)'

            if not re.match (ACCOUNT_REGEX, account):
                  return JsonResponse({'message':'INVALID_FORMAT'}, status=400) 
            if User.objects.filter(account = account).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'}, status=400)
            return JsonResponse({'message':'SUCCESS'}, status=200) 
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignUpView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)       
            name     = data['name']
            account  = data['account']
            mobile   = data['mobile']
            address  = data['address']
            email    = data['email']
            password = data['password']
            
            ACCOUNT_REGEX   = '(^(?=.*[a-z])(?=.*\d)[a-z\d]{6,20}$)'
            PASSWORD_REGGEX = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^~@$!%*#?&])[A-Za-z\d^~@$!#%*?&]{8,20}$'
            MOBILE_REGEX    = '^[0-9]{3}[0-9]{4}[0-9]{4}$'
            EMAIL_REGEX     = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
            NAME_REGEX      = '^[가-힣]+'
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if ('' == account) or ('' == password):
                return JsonResponse({'message':'VALUE_IS_EMPTY'}, status=400)
            if not re.match(ACCOUNT_REGEX, account) or\
               not re.match(PASSWORD_REGGEX, password) or\
               not re.match(MOBILE_REGEX, mobile) or\
               not re.match(NAME_REGEX, name) or\
               not re.match(EMAIL_REGEX, email):
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
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
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