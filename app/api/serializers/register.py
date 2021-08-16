from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer


class RegisterSerializer(DefaultRegisterSerializer):
    username = None
