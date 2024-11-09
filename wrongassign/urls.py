"""
URL configuration for wrongassign project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]

# url에 대한 매핑을 추가함. 위에 user app과의 관계는 userapp/urls.py가 config/urls.py을 참조함
# 프로젝트 전체의 URL 구조를 정의하는 거라고 보면 됨
# 모든 프로젝트의 URL패턴은 이 파일에서 시작되서 각기 앱에 urls.py로 위임됨