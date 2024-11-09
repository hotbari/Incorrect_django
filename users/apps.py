from django.apps import AppConfig


class UsersConfig(AppConfig):   #UsersConfig을 만들거야, 그리고 (appconfig)을 상속 받을거임
    default_auto_field = 'django.db.models.BigAutoField'    #이 앱에 기본 설정은 값이 자동으로 증가하는 필드임
    name = 'users'  #이 앱 이름은 users로 할거임



    # 각 애플리케이션에 대한 항목을 설정하는 곳