## 가상환경
독립된 공간 (각 프로젝트가 영향 받지 않음)  
**가상환경 안에서 장고를 깔았으면 다른 가상환경에선 연동이 안됨**  
### 가상환경 작성
> python -m venv <가상환경이름>  

venv = virtual environment  

### 가상환경 실행
> source <가상환경이름>/Scripts/activate
### 가상환경 종료
> deactivate

## pip 패키지
파이썬으로 작성된 패키지 소프트웨어를 설치, 관리하는 패키지 관리 시스템  
Django = pip 패키지  

### 장고 설치
> pip install django

### 장고 삭제
> pip uninstall django

### 특정 버전 장고 설치
> pip install django==<버전>

## vscode 팁
### bash로 변경
> select default shell, git bash에서 code .

# Django
### 장고 프로젝트 생성
> django-admin startproject <project 이름>

### 장고 서버 작동
> python manage.py runserver

## App
프로젝트의 구성 단위  
App 은 안 만들어도 되는 상황이어도 만들어두는 편이 코드 가용성을 위해 좋음

### App 생성
> python manage.py startapp <app 이름>

App 폴더 안에 'templates' 폴더 따로 만들어줘야 함  
**'templates'** 폴더 안에 유저에게 보여질 화면들 (html) 담기

App 생성 후 프로젝트의 settings.py 에 알려야 함

### INSTALLED_APPS 에 추가
> <app이름>.apps.<첫글자대문자app이름>Config

templates 안의 유저에게 보여질 화면 (html)이 언제, 어떻게 처리될지 알려주는 함수 추가해야 함

### views.py 에 추가
```
def home(request):
    return render(request, <템플릿 이름>, <딕셔너리>)
```

내가 만든 html이 어떤 url을 입력했을 때 뜨게 할지 알려야 함

### url.py 에 추가
path('', myapp.views.home, name="home")
이름 정하는 이유: 함수이름이 바뀔 수도 있으므로

### 템플릿 변수
> {{ python_value }}
### 템플릿 필터
#### 템플릿 변수에 추가적인 속성 및 기능 제공  
> {{ python_value | filter }}

#### 길이
> {{ value | length }}

#### 소문자로
> {{ value | lower }}

### 템플릿 태그
#### html 상에서 파이썬 문법 사용, url생성 등의 기능 제공
> {% tag %} ... 태그 내용 ... {% endtag %}

#### 예시
> {% for students in class %} {{students}} {% endfor %}

> {% url 'url_name' %}

**템플릿 상속 참고**

### 입력받은 값
> request.GET['<입력한 값>']