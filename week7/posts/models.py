from django.db import models

# Create your models here.

class Post (models.Model):
    image=models.ImageField(verbose_name='이미지')
    content=models.TextField('내용')
    created_at=models.DateTimeField('작성일')
    view_count=models.IntegerField('조회수')

class Reply (models.Model):
    writer=models.CharField(max_length=20)
    content=models.TextField('내용')
    created_at=models.DateTimeField('작성일') 
    #이렇게 클래스 정의 후 migration 해주고 admin.py에 임포트해줌