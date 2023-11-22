# 🔖목차
- [초기 설정](docs/init.md)
- [User](docs/auth_user.md)

## 📁프로젝트 디렉토리 구조
```console
🖥️prj
├─🔨config
├─🌐coverletter_site
├─📁media
│  └─📁documents
│  └─📁review
├─🌐member_site
├─🌐review_site
├─📁static
│  ├─📃css
│  ├─📃images
│  └─📃js
├─📁templates
│   ├─📃base
│   ├─📃coverletter_site
│   ├─📃member
│   └─📃review_site
│   └─📃web_site
└─🌐review_site
```
- `config/` : 장고 프로젝트 디렉토리
- `coverletter_site/` : 장고 웹 앱 디렉토리
    - `templates/` : 동적 웹 리소스
        - `base/` : 웹 페이지의 뼈대가 되는 html 파일 모음
- `media/` : 웹상의 업로드된 파일을 저장하는 디렉토리
    - `documents/` : 자소서 문서
    - `review/` : 리뷰 페이지에서 사용자가 업로드한 파일
- `static/` : 정적 웹 리소스
        - `css/` : css 모음
        - `js/` : 자바스크립트 모음

## 🔨`settings.py`

- 앱 장고에 등록
    ```py
    INSTALLED_APPS = [
    'web_site.apps.WebSiteConfig',
    'coverletter_site.apps.CoverletterSiteConfig',
    'member_site.apps.MemberSiteConfig',
    'review_site.apps.ReviewSiteConfig',
    # ...
    'crispy_forms',
    'crispy_bootstrap4',
    ]
    ```
    - `coverletter_site.apps.CoverletterSiteConfig`: 자소서 표절 검증
    - `member_site.apps.CoverletterSiteConfig`: 회원 기능
    - `review_site.apps.CoverletterSiteConfig`: 이용 후기
    - `web_site.apps.CoverletterSiteConfig`: 메인 페이지, 글자 수 세기, 맞춤법 검사 등
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

- 회원의 모델 지정과 로그인, 로그아웃 성공 시, 이동할 URL
    ```py
    AUTH_USER_MODEL = 'member_site.User'
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"
    ```

- 업로드한 파일의 디렉토리 경로와 URL 지정
    ```py
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    ```

- 정적 페이지(css, js) 디렉토리 경로 지정
    ```py
    STATICFILES_DIRS = [BASE_DIR / 'static']
    ```

- 템플릿 페이지(html) 디렉토리 경로 지정
    ```py
    TEMPLATES = [
        'DIRS': [BASE_DIR / 'templates'],
    ]
    ```

- Crispy-bootstrap4 세팅
    ```py
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
    CRISPY_TEMPLATE_PACK = "bootstrap4"
    ```

## 📬URI 매핑

- `config/urls.py`
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('web_site.urls')),
        path('coverletter/', include('coverletter_site.urls')),
        path('', include('member_site.urls')),
        path('review/', include('review_site.urls')),
    ]
    ```
    - `host:port/` : 메인 페이지
    - `host:port/login/` : 로그인 페이지
    - `host:port/logout/`: 로그아웃 페이지
    - `host:port/join/`: 회원 가입 페이지
    - `host:port/upload/`: 자소서 업로드 페이지
    - `host:port/result_list/`: 표절 자소서 검증 결과 목록 페이지