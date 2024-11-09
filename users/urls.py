from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]#/users/pk/ 로 접속하면 userdetail이라는 클래스의 인스턴스를 만듦, as_view()로 매서드를 호출해서 뷰 함수처럼 실행.
# 이 패턴에 대한 이름을 지정함. 다른 곳에서 이 패턴을 참조할 수 있도록.

# 프로젝트 안에서 생성된 모든 view들에게 url을 할당해주고 요청이 발생하면 구현한 함수대로 코드가 실행될 수 있게 함
# 어플리케이션을 구현하고자 할 때 urls.py에 url을 알려줘야함