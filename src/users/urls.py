from django.urls import path
from users.views import SignUpPageView, LoginPageView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('sign_up/', SignUpPageView.as_view(), name='sign_up'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),
]