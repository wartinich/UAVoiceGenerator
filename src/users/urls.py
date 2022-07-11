from django.urls import path
from users.views import RegisterPageView, LoginPageView, UpdateUserView, DeactivateUser
from django.contrib.auth import views as auth_views
from users.forms import CustomChangePasswordForm, CustomResetPasswordForm

urlpatterns = [
    path('sign_up/', RegisterPageView.as_view(), name='sign_up'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/index.html'), name='logout'),
    path('deactivate/', DeactivateUser.as_view(), name='deactivate_user'),

    path('profile/', UpdateUserView.as_view(), name='profile'),

    # Change password
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
            template_name='profile/change_password.html',
            success_url='/profile/',
            form_class=CustomChangePasswordForm
         ),
        name='change_password'),

    # Reset Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auth/password_reset/password_reset_form.html',
             subject_template_name='auth/password_reset/password_reset_subject.txt',
             email_template_name='auth/password_reset/password_reset_email.html',
             form_class=CustomResetPasswordForm
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auth/password_reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auth/password_reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/login.html'
         ),
         name='password_reset_complete'),
]