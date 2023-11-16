#
- [초기 설정](docs/init.md)

## 📁프로젝트 디렉토리 구조
```

```

## ⚙️`settings.py`

- 앱 장고에 등록
```py
INSTALLED_APPS = [
   'coverletter_site.apps.CoverletterSiteConfig',
   # ...
   'crispy_forms',
   'crispy_bootstrap4',
]
```
    - `coverletter_site.apps.CoverletterSiteConfig`: 자소서 표절 검증 사이트 앱
    - `crispy_forms, crispy_bootstrap4` : HTML 폼 태그, 부트스트립 css 자동 적용 시켜주는 라이브러리

- 데이터 베이스 설정
``` py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bigdata_django_prj',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
    - `ENGINE` : MySql
    - `NAME` : 데이터베이스명
    - `USER`, `PASSWORD` : 수업 때 만들었던 django라는 계정을 사용해도 무방함.
    - `HOST`, `PORT` : MySql 설치 시 기본으로 설정된 호스트와 포트 번호를 씀.

- 로그인 성공 후, 리다이렉션 세팅
```PY
LOGIN_REDIRECT_URL = "/"
```

- Crispy-bootstrap4 세팅
```py
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"
```