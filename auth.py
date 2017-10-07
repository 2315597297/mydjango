from user_online.models import User


class MyCustomBackend:
    def authenticate(self, nicheng=None, business_password=None):
        try:
            user = User.objects.get(nicheng=nicheng)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(business_password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None