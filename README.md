# [쪽지시험 미달자신가요?]
Django 쪽지시험 미달자들의 오답노트용 레포지토리입니다.  
해당 레포지토리를 클론 받고 하단의 파일들의 모든 코드에 한 줄씩 주석을 달아주세요.  

### 1. users APP
- admin.py 
    # startapp하면 나오는 애들 중, 이 앱에서 발생하는 데이터와 같이 관리자가 쉽게 접근할 수 있도록 하는 경우엔 admin.py에 작성해야함
    # admin.py 파일은 관리자가 데이터베이스 모델을 관리하는 데 사용되는 파일임
- apps.py
    # 각 애플리케이션에 대한 항목을 설정하는 곳
- models.py
    # django framwork에서 데이터모델을 만들어주는 파일임. 여기서 모델을 만들어주면 장고가 ORM을 통해 데이터베이스에 데이터모델을 생성해줌
- serializers.py
    # 직렬화 해주는 것. 서버에서 클라이언트에 보내줄 데이터를 정해진 형식으로 바꿔주는 것을 말한다.
- urls.py
    # 프로젝트 안에서 생성된 모든 view들에게 url을 할당해주고 요청이 발생하면 구현한 함수대로 코드가 실행될 수 있게 함
    # 어플리케이션을 구현하고자 할 때 urls.py에 url을 알려줘야함
- views.py
    # 사용자가 입력한 url에 따라 model에서 필요한 데이터를 가져와 뷰에서 보여주며, 템플릿에 전달해줌

### 2.wrongassign (config 역할입니다.)
- settings.py
    # 프로젝트 설정 파일, 처음 프로젝트 생성하면 기본 사항이 담겨있음.
- urls.py
    # url에 대한 매핑을 추가함. 위에 user app과의 관계는 userapp/urls.py가 config/urls.py을 참조함
    # 프로젝트 전체의 URL 구조를 정의하는 거라고 보면 됨
    # 모든 프로젝트의 URL패턴은 이 파일에서 시작되서 각기 앱에 urls.py로 위임됨

### 3. manage.py 의 역할. 
- 프로젝트 관리 및 작업 수행 개발 서버 실행
- 웹 앱을 로컬 환경에서 테스트
```
python manage.py runserver
```
- 데이터베이스 마이그레이션
- 데이터베이스 스키마를 변경하고 새로운 모델을 적용
```
python manage.py migrate
```
- 관리자 계정 생성
```
python manage.py createsuperuser
```
- 데이터베이스에 모든 데이터 초기화
```
python manage.py flush
```
- 테스트 케이스를 실행
```
python manage.py test
```
- 컬렉션 관리
- 정적 파일 수집 or 프로젝트 상태 확인 등 다양한 작업 수행 가능
### 4. __init__.py 의 역할  

#### 특정 디렉토리를 패키지로 인식하게 해준다
```
from .models import * #.models에서 모듈 *(전부)를 가져온다.
from .views import * #.views에서 모듈*(전부)를 가져온다.

__all__ = ['models', 'views'] # models와 views에서 가져온 모듈을 __all__에 담는다.
```
- 일관된 인터페이스 제공 가능
- 편리함
- 단, 실제로 사용하지 않는 모듈까지 임포트 될 수 있ㄷk
