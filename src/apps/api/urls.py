from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from djoser.views import UserViewSet
from apps.api.views import RecordViewSet


urlpatterns = [
    # Auth
    path('sign_up/', UserViewSet.as_view({'post': 'create'})),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Profile
    path('user/me/', UserViewSet.as_view({'get': 'me'})),
    path('user/me/update/', UserViewSet.as_view({'patch': 'me', 'put': 'me'})),

    # Password reset
    path('password_reset/', UserViewSet.as_view({'post': 'reset_password'})),
    path('password_reset/confirm/', UserViewSet.as_view({'post': 'reset_password_confirm'})),

    # Password change
    path('change_password/', UserViewSet.as_view({'post': 'set_password'})),

    # Records
    path('record_history/', RecordViewSet.as_view({'get': 'list'}), name='record_history'),
    path('generate/', RecordViewSet.as_view({'post': 'create'}))

]