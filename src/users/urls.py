from django.urls import path
from users.views import SignUpPageView, LoginPageView


urlpatterns = [
    path('sign_up', SignUpPageView.as_view(), name='sign_up'),
    path('login', LoginPageView.as_view(), name='login')
]