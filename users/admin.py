from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # 관리자 페이지에 표시할 필드 설정
    search_fields = ('name', 'email')  # 검색 가능 필드 설정


    # startapp하면 나오는 애들 중, 이 앱에서 발생하는 데이터와 같이 관리자가 쉽게 접근할 수 있도록 하는 경우엔 admin.py에 작성해야함
    # admin.py 파일은 관리자가 데이터베이스 모델을 관리하는 데 사용되는 파일임