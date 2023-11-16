#

## 📁프로젝트 디렉토리 구조
```

```

## ⚙️`settings.py`

- 앱 장고에 등록
```py
INSTALLED_APPS = [
   'coverletter_site.apps.CoverletterSiteConfig',
   # ...
]
```

- 데이터 베이스 설정
``` py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'big_data_django_prj',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
    - `ENGINE` : MySql
    - `NAME` : 데이터베이스명