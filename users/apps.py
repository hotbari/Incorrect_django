from django.apps import AppConfig

# Users 앱의 구성 클래스를 정의합니다.
# Django 는 각 앱마다 설정 정보를 포함하는 Config 클래스를 찾습니다.
class UsersConfig(AppConfig):

    # 기본 필드 타입으로 BigAutoField를 사용하도록 설정합니다.
    # 이 설정은 각 모델의 기본 ID 필드에 적용됩니다.
    default_auto_field = 'django.db.models.BigAutoField'

    # 앱의 이름을 지정합니다. 여기서는 'users' 라는 이름으로 앱을 식별합니다.
    name = 'users'



class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


