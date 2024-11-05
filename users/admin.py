from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # 관리자 페이지에 표시할 필드 설정
    search_fields = ('name', 'email')  # 검색 가능 필드 설정
