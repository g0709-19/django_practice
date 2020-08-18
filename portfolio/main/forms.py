from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('profile', 'title', 'content', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile'].label = '사진'
        self.fields['title'].label = '제목'
        self.fields['content'].label = '내용'
        for item in ('profile', 'title', 'content'):
            self.fields[item].widget.attrs.update({
                'class': 'form-control',
            })
        