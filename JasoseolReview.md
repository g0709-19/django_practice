# 자소설닷컴 정리
멋쟁이사자처럼 자소설닷컴 강의 내용 정리

## Model & DB
### Field
|||
|---|---|
| Primary Key | AutoField |
| 문자열 | CharField, TextField, SlugField |
| 숫자 | IntegerField, PositiveIntegerField, FloatField |
| 날짜/시간 | DateField, TimeField, DateTimeField |
| 참/거짓 | BooleanField, NullBooleanField |
| 파일 | FieldField, ImageField, FilePathField |

### display flex
요소 컨트롤 가능

1. CSS 에서 display: flex 추가
2. flex: 1 # 1대1 비율
3. flex-direction: column # 가로로 한칸씩 차지
4. align-items: center # 가운데 정렬
5. display: inline-flex # 블록이 아닌 인라인으로 처리

**rem == 기본 정의된 사이즈의 배수**

### ModelForm
* 모델에 대응하는 html폼을 만들어 줌
* 데이터를 생성하거나 업데이트가 간편
* 폼을 다루는 법을 배워야 함

#### 앱 폴더 내에 forms.py 생성
#### views.py 에서 from .forms import Form
#### html 에서 form 불러온 뒤 .as_p 하면 p태그로 감쌈
#### form 태그 action 비워주면 해당 페이지의 url 실행

### Primary Key
오브젝트를 식별할 수 있는 값, 중복될 수 없는 단일 값
```
my_pk = models.IntegerField(primary_key=True)
```

### Form(instance=오브젝트) # 오브젝트 가리키는 폼
### Form(request.POST) # POST 로 받아온 내용 포함해서 폼 생성
### Form(request.POST, instance=오브젝트) # 오브젝트 가리키는 폼에 POST 로 받아온 내용 포함

### 없는 오브젝트 참조 시
```
from django.http import Http404

try:
    # getObject
except:
    raise Http404
```