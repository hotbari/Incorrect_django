# [쪽지시험 미달자신가요?]
Django 쪽지시험 미달자들의 오답노트용 레포지토리입니다.  
해당 레포지토리를 클론 받고 하단의 파일들의 모든 코드에 한 줄씩 주석을 달아주세요.  

### 1. users APP
- admin.py
- apps.py
- models.py
- serializers.py
- urls.py
- views.py

### 2.wrongassign (config 역할입니다.)
- settings.py
- urls.py

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
