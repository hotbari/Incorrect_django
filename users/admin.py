from django.contrib import admin
from .models import User

# Register your models here.
# admin 데코레이터를 사용해 User 모델을 관리자 페이지에 등록
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 관리자 페이지에 표시할 필드 설정
    # id, name, email 필드를 테이블 형태로 보여줌.
    list_display = ('id', 'name', 'email')
    # 검색 가능 필드 설정
    # name 과 email 필드에서 검색이 가능하도록 설정
    search_fields = ('name', 'email')



@ admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
