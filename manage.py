#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wrongassign.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#프로젝트의 설정 파일 (wrongassign.settings in this case)을 로딩하여 Django 환경을 설정
#django-admin 명령과 함께 사용되어 데이터베이스 마이그레이션, 서버 실행, 테스트 수행
#Django 설정 오류가 발생시 에러 메시지 출력