from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import ResendEmailVerificationView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import LogoutView
from dj_rest_auth.views import PasswordChangeView
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.views import PasswordResetView
from dj_rest_auth.views import UserDetailsView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import include
from django.urls import path

app_name = 'auth'

registration = [
    path('', RegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name='rest_resend_email'),
]

urlpatterns = [
    # path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/', include(registration)),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # URLs that do not require a session or valid token
    # path('login/', LoginView.as_view(), name='rest_login'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),

    # URLs that require a user to be logged in with a valid session / token.
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
]
