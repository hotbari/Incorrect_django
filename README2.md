3. manage.py 의 역할.
장고 프로젝트의관리 및 실행을 도와주는 스크립트
    1. 프로젝트 관리
    2. 명령 실행 
        - runserver : 서버 실행
        - migrate : 데이터베이스 마이그레이션
        - makemigrations : 모델 변경 사항 반영
        - createsuperuser : 관리자 생성
        - shell : 장고 쉘 실행
    3. 환경 설정
        - 장고의 설정 모듈을 로드하여 프로젝트 환경을 설정

4. init.py 의 역할.
파이썬 패키지를 정의하는데 사용되는 파일
장고 프로젝트 내에서 앱과 모듈의 구조를 정의하고 초기화하는 중요할 역할을 함
    1. 패키지 식별
        - init.py 파일이 존재하는 디렉토리는 파이썬에게 해당 디렉토리가 패키지임을 알린다. 
        - 이로 인해 해당 디렉토리 내의 모듈을 다른 모듈에서 임포트 할 수 있다.
    2. 초기화 코드 실행
        - 패키지를 임포트 할 때 init.py 파일 내에 정의된 코드가 실행됩니다.
        - 여기서 초기화 작업이나 패키지 전반에 걸쳐 필요한 설정을 할 수 있다.
    3. 모듈 공개
        - init.py 파일 내에서 __all__ 변수를 정의함으로써 패키지가 임포트 될 때 어떤 모듈이나 변수를 공개할지 지정할 수 있다.
        - 이 경우 from package import * 를 사용했을 때 module1과 module2만 임포트 됩니다.
    ```python
    __all__ = ['module1', 'module2']
    ```
    4. 다양한 구조
        - 서로 독립적으로 작동하면서도 필요한 경우 다른앱과 상호작용 할 수 있다.


