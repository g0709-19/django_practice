from django.db import models

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField() # max_length 필수 아님
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 되거나 할 때 시간을 자동 저장

    def __str__(self):
        return self.title