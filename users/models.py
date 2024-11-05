from django.db import models

# Create your models here.
# User 모델을 정의합니다. 데이터베이스 테이블을 나타냅니다.
class User(models.Model):
    # name 을 저장하는 필드이고, 최대 100문자의 문자열을 허용합니다.
    name = models.CharField(max_length=100)
    # email 을 저장하는 필드이고, 이메일 형식이어야 하고, 유니크(고유)해야 합니다.
    email = models.EmailField(unique=True)


    # 객체를 문자열로 표현할 때 호출되는 메서드
    def __str__(self):
        # User 객체의 name을 반환합니다.
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name