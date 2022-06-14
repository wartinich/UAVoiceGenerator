from django.urls import path
from users.views import RegisterPageView, LoginPageView, UpdateUserView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from users.forms import CustomChangePasswordForm

urlpatterns = [
    path('sign_up/', RegisterPageView.as_view(), name='sign_up'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),

    path('profile/', UpdateUserView.as_view(), name='profile'),

    # Change password
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
            template_name='profile/change_password.html',
            success_url = '/profile/',
            form_class = CustomChangePasswordForm
         ),
            name='change_password'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]