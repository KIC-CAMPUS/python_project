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