# 초기 설정

## 📦파이썬 라이브러리
- 장고
    ```console
    > pip install Django==4.2.7
    ```
- Mysql
    ```console
    > pip install mysql
    ```
- [Crispy form](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
    ```console
    pip install django-crispy-forms
    pip install crispy-bootstrap4
    ```

- 판다스
    ```console
    pip install pandas
    ```

- 한국어 형태소 분리기
    ```console
    pip install konlpy
    ```
- 자연어 처리 라이브러리
    ```
    pip install nltk
    ```
    
## 💻장고 프로젝트 생성
- 프로젝트 디렉토리 생성
    ```console
    ../prj> django-admin startproject config .
    ```
- `resume_site` 앱 디렉토리 생성
    ```console
    ../prj> django-admin startapp resume_site
    ```
- mysql 데이터 베이스 생성
    ```console
    > mysql -u root -p
    Enter password: ******

    mysql> create database bigdata_django_prj default character set UTF8;
    Query OK, 1 row affected, 1 warning (0.00 sec)
    ```

## 🗄️데이터 베이스 마이그레이션
- makemigrations
    ```console
    ../prj> python manage.py makemigrations
    ```
- migrate
    ```console
    ../prj> python manage.py migrate
    ```

## 🏃장고 서버 시작
- runserver
    ```console
    ../prj> python manage.py runserver
    ```

## 🧑‍💼관리자 계정 생성
- createsuperuser
    ```console
    ../prj> python manage.py createsuperuser
    ```