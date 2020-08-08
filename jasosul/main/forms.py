from django import forms
from .models import Jasoseol

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