from django.urls import path
from .views      import SignUpView,AccountCheckView,SignInView

urlpatterns = [
    path('/account-validator', AccountCheckView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view())

]