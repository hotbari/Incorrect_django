
# Django REST Framework 의 serializers 모듈
from rest_framework import serializers
from .models import User

# User 모델을 위한 직렬화 클래스.
# ModelSerializer 를 상속받아 모델의 필드를 자동으로 처리.
class UserSerializer(serializers.ModelSerializer):
    # 직렬화 클래스의 메타데이터를 정의
    class Meta:
        # 직렬화 할 모델을 지정한다. 여기서는 User 모델
        model = User
        # 직렬화할 필드를 지정. '__all__' 을 사용해 모든 필드를 포함
        fields = '__all__'


class UserSErializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

