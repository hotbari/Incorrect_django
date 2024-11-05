"""
Django settings for wrongassign project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# 프로젝트의 기본 디렉토리 경로를 설정
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# 시크릿 키, 프로덕션 환경에서 비밀로 유지해야 함.
SECRET_KEY = 'django-insecure-3mxtvqvp49$q9s-rx6+86svzg41qf=#)!19kb(=6wv_yr=y54q'

# SECURITY WARNING: don't run with debug turned on in production!

# 디버그 모드 활성화
# 프로덕션 환경에서는 False로 설정
DEBUG = True

# 요청을 허용할 호스트 목록, 프로덕션에서는 적절히 설정해야 함.
ALLOWED_HOSTS = []


# Application definition

# 설치된 애플리캐이션 목록
INSTALLED_APPS = [
    'django.contrib.admin', # Django의 admin 사이트 기능
    'django.contrib.auth',  # 인증 시스템
    'django.contrib.contenttypes',  # 콘텐츠 유형 프레임 워크
    'django.contrib.sessions',  # 세션 관리
    'django.contrib.messages',  # 메시지 프레임 워크
    'django.contrib.staticfiles',   # 정적 파일 관리
    'users',    # users 앱
]

# 미들웨어 목록
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',     # 보안 관련 미들웨어
    'django.contrib.sessions.middleware.SessionMiddleware',    # 세션 미들 웨어
    'django.middleware.common.CommonMiddleware',    # 공통 미들 웨어
    'django.middleware.csrf.CsrfViewMiddleware',    # CSRF 방지 미들웨어
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 인증 미드웨어
    'django.contrib.messages.middleware.MessageMiddleware',     # 메시지 미들웨어
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # 클릭 재킹 방지 미들웨어
]

# URL 패턴을 정의한 모듈
ROOT_URLCONF = 'wrongassign.urls'

# 템플릿 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # 템플릿 백엔드 설정
        'DIRS': [BASE_DIR / 'templates']    # 템픞릿 디렉토리 경로
        ,
        'APP_DIRS': True,   # 앱 내 템플릭 디렉토리를 사용할지 여부
        'OPTIONS': {
            'context_processors': [     # 템플릿에서 사용할 컨텍스트 프로세서
                'django.template.context_processors.debug',     # 디버깅 정보
                'django.template.context_processors.request',   # 요청 정보
                'django.contrib.auth.context_processors.auth',  # 인증 정보
                'django.contrib.messages.context_processors.messages',  # 메시지 정보
            ],
        },
    },
]

# WSGI 애플리케이션 설정
WSGI_APPLICATION = 'wrongassign.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# 데이터베이스 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # 데이터베이스 엔진
        'NAME': BASE_DIR / 'db.sqlite3',        # 데이터베이스 파일 경로
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [    # 비밀번호 유효성 검사기 목록
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # 사용자 속성 유사성 검사기
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',   # 최소 길이 검사기
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 일반 비밀번호 검사기
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # 숫자 비밀번호 검사기
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us' # 기본 언어 코드

TIME_ZONE = 'UTC'   # 시간대 설정

USE_I18N = True # 국제화 사용 여부

USE_TZ = True   # 시간대 사용 여부


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'  # 정적(STATIC) 파일의 URL 경로

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field


# 기본 키 필드 유형 설정
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
