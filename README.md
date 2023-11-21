# 🔖목차
- [초기 설정](docs/init.md)
- [User](docs/auth_user.md)

## 📁프로젝트 디렉토리 구조
```console
🖥️prj
├─📁config
└─📁coverletter_site
    ├─📁static
    │  ├─📁css
    │  └─📁js
    └─📁templates
       └─📁coverletter_site
           └─📁base
```
- `config/` : 장고 프로젝트 디렉토리
- `coverletter_site/` : 장고 웹 앱 디렉토리
    - `static/` : 정적 웹 리소스
        - `css/` : css 모음
        - `js/` : 자바스크립트 모음
    - `templates/` : 동적 웹 리소스
        - `base/` : 웹 페이지의 뼈대가 되는 html 파일 모음

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

- 로그아웃 성공 후, 리다이렉션 URL 지정
    ```py
    LOGOUT_REDIRECT_URL = "/"
    ```

- 업로드한 파일의 디렉토리 경로 지정
    ```py
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    ```

- 정적 페이지(css, js) 디렉토리 경로 지정
    ```py
    STATICFILES_DIRS = [BASE_DIR / 'static']
    ```

- Crispy-bootstrap4 세팅
    ```py
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
    CRISPY_TEMPLATE_PACK = "bootstrap4"
    ```

## 📬URI 매핑

- `coverletter_site/urls.py`
    ```py
    from django.urls import path
    from django.contrib.auth import views as auth_views
    from . import views

    urlpatterns = [
        path("", views.index, name='main'),
        path("login/", auth_views.LoginView.as_view(template_name='coverletter_site/login.html'), name='login'),
        path("logout/", auth_views.LogoutView.as_view(), name='logout'),
        path("join/", views.join, name='join'),
        path("upload/", views.coverletter_upload, name='upload'),
        path("result_list/", views.CoverLetterList.as_view(), name='result_list'),
    ]
    ```
    - `host:port/` : 메인 페이지
    - `host:port/login/` : 로그인 페이지
    - `host:port/logout/`: 로그아웃 페이지
    - `host:port/join/`: 회원 가입 페이지
    - `host:port/upload/`: 자소서 업로드 페이지
    - `host:port/result_list/`: 표절 자소서 검증 결과 목록 페이지