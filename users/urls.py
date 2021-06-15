from django.urls import path
from .views      import SignUpView, AccountCheckView

urlpatterns = [
    path('/account-validator', AccountCheckView.as_view()),
    path('/signup', SignUpView.as_view())
]