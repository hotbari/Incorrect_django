from django.db import models # Django 모델 관련 클래스를 가져옵니다.


class User(models.Model): # User 모델을 정의합니다. Django의 기본 모델을 상속받습니다.
    name = models.CharField(max_length=100) # 사용자의 이름을 문자열로 저장합니다. 제한길이는 100자입니다.
    email = models.EmailField(unique=True) # 사용자의 이메일을 이메일 필드로 저장합니다. unique=True 옵션으로 인해 중복값을 허용하지 않습니다.

    def __str__(self): # User 객체를 문자열로 반환할 때
        return self.name # User의 이름을 반환합니다.