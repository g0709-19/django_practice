# 자소설닷컴 정리
멋쟁이사자처럼 자소설닷컴 강의 내용 정리

# Model & DB
## Field
|||
|---|---|
| Primary Key | AutoField |
| 문자열 | CharField, TextField, SlugField |
| 숫자 | IntegerField, PositiveIntegerField, FloatField |
| 날짜/시간 | DateField, TimeField, DateTimeField |
| 참/거짓 | BooleanField, NullBooleanField |
| 파일 | FieldField, ImageField, FilePathField |

### DateTimeField
자동으로 현재 시간
> auto_now=True

템플릿 필터
> date:"Y-m-d"

settings.py
```
LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul'
```

### display flex
요소 컨트롤 가능

1. CSS 에서 display: flex 추가
2. flex: 1 # 1대1 비율
3. flex-direction: column # 가로로 한칸씩 차지
4. align-items: center # 가운데 정렬
5. display: inline-flex # 블록이 아닌 인라인으로 처리

**rem == 기본 정의된 사이즈의 배수**

## ModelForm
* 모델에 대응하는 html폼(block)을 만들어 줌
* 데이터를 생성하거나 업데이트가 간편
* 폼을 다루는 법을 배워야 함

#### 앱 폴더 내에 forms.py 생성
#### from django import forms
#### views.py 에서 from .forms import Form
#### html 에서 form 불러온 뒤 .as_p 하면 p태그로 감쌈
#### form 태그 action 비워주면 해당 페이지의 url 실행

```
class JssForm(forms.ModelForm):
    class Meta:
        model = Jasoseol # 어떤 모델과 대응될 지
        fields = ('title', 'content', ) # 모델을 대응시키는 폼을 만들 때 어떤 것들만 만들 지

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['content'].label = '자기소개서 내용'
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder': '제목',
        })
```

## Primary Key
오브젝트를 식별할 수 있는 값, 중복될 수 없는 단일 값
```
my_pk = models.IntegerField(primary_key=True)
```

#### Form(instance=오브젝트) # 오브젝트 가리키는 폼, update 에서 쓰임
#### Form(request.POST) # POST 로 받아온 내용 포함해서 폼 생성
#### Form(request.POST, instance=오브젝트) # 오브젝트 가리키는 폼에 POST 로 받아온 내용 포함

### 없는 오브젝트 참조 시
```
from django.http import Http404

try:
    <Model>.objects.get(pk=<PK>)
except:
    raise Http404
```

## UserModelForm
```
# 회원가입 폼
from django.contrib.auth.forms import UserCreationForm
UserCreationForm()
```
form action 값 없으면 그 페이지를 렌더링시킨 함수를 사용

```
from django.contrib.auth.views import LoginView
LoginView.as_view() # urls.py 에서 사용시 as_view 필수(클래스기 때문)
```

#### templates/registration/login.html 추가
#### {{ form }} 로그인 폼
#### LOGIN_REDIRECT_URL -> setting.py
#### {{ user }} 유저 확인, 없으면 AnonymousUser
#### {{ user.is_authenticated }} 로그인 확인

### Override
views.py 에서 클래스 생성 후 LoginView 상속

## ForeignKey
어떤 모델의 객체와 다른 모델의 객체의 일대다 대응 관계를 형성하는 기능
```
# 연결된 모델이 삭제되면 같이 삭제되도록 연결
author = models.ForeignKey(<Model>, on_delete=models.CASCADE, null=True)
```
#### null=True 없이 makemigrations 하면 오류! 이미 있던 객체들의 author 의 기본값 설정 방식을 제시하지 않았기 때문(default=<계정이름> 도 가능)

### 객체 저장 지연
```
temp_form = filled_form.save(commit=False) # 객체 저장 지연
temp_form.author = request.user # user 정보 대입
temp_form.save() # 객체 저장
```

### 접근 제한 페이지
```
from django.core.exceptions import PermissionDenied
raise PermissionDenied
```

### login_required
```
# 로그인 필요시 login_url로 이동
from django.contrib.auth.decorators import login_required
@login_required(login_url='')
def ~~~
```

### objects.filter
```
# Jasoseol 모델의 author 필드가 request.user 인 객체만 필터링
my_jss = Jasoseol.objects.filter(author=request.user)
```

## ORM
* 객체(Object)와 관계형 데이터베이스(Relational Database)의 데이터를 매핑(Mapping)해주는 것
* 객체 간의 관계를 바탕으로 SQL을 자동으로 생성해서 SQL 쿼리문 없이도 데이터베이스의 데이터들을 다룰 수 있음

<a href="https://fabl1106.github.io/django/2019/05/27/Django-26.-%EC%9E%A5%EA%B3%A0-related_name-%EC%84%A4%EC%A0%95%EB%B0%A9%EB%B2%95.html">참고</a>

models.py
```
    models.ForeignField(<Model>, on_delete=models.~~~, related_name='<Name>')
```

template
```
    <Model>.<Name>.all
```

## Javascript
script src="{% url 'js/count.js' %}"

### 요소 선택
```
querySelector(<selector>)
```

### 이벤트 핸들러
```
<Element>.addEventListener("<Event>", <Function>)
```
