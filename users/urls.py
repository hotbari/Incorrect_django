from django.urls import path
from .views import UserList, UserDetail

# url 패턴을 정의
urlpatterns = [

    # users/ 경로 정의, UserList 뷰를 사용하여 템플릿을 보여준다. url name 은 user-list 로 정의
    path('users/', UserList.as_view(), name='user-list'),

    # users/<int:pk>/ 경로 정의, <int:pk>는 정수형 primarykey를 정의
    # UserDetail 뷰를 사용하여 템플릿을 보여준다. url name 은 user-detail 로 정의
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]



urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]