from django.db import models

# Create your models here.
class User(models.Model):   #User라는 클래스를 만들거고 models(모듈).model(클래스) 즉 모듈 안에 클래스를 상속 받을게
    name = models.CharField(max_length=100) #User라는 클래스에 name은 문자형이고, Models.가 있기에 데이터베이스랑 상호작용 가능해(?) 제한은 100
    email = models.EmailField(unique=True)  #User라는 클래스에 email은 email필드로 만들 거고, unique(유일한 값)으로 만들게

    def __str__(self):      #함수 정의할게, __str__은 매직 메소드야. 객체 출력할 때 문자열로 출력할 거고 객체는 self(자기자신)이야#
        return self.name    #결과를 리턴할게, 객체에 name에 속성값을 반영할

    # django framwork에서 데이터모델을 만들어주는 파일임. 여기서 모델을 만들어주면 장고가 ORM을 통해 데이터베이스에 데이터모델을 생성해줌