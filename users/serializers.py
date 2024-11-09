from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):  #UserSerializer라는 클래스 정의(상속받을 매개변수는 JsoN형식으로 변환해
    class Meta: #(시리얼라이저가 어떤 모델을 기반으로 동작할지, 어떤 필드에 포함해야하는지 말해줄 거임)
        model = User    #이 시리얼라이즈에 모델은 user임.user모델의 인스턴스를 JSON형식으로 변환할거임
        fields = '__all__'  # user모델의 모든 필드를 시리얼라이저함. 즉 json형식으로 변환할 때 해당 모델과 같이 있는 모든 필드값을 말함