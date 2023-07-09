from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User=get_user_model()

class Post (models.Model):
    image=models.ImageField(verbose_name='이미지')
    content=models.TextField('내용')
    created_at=models.DateTimeField('작성일', auto_now_add=True)
    view_count=models.IntegerField('조회수', default=0)
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자', null=True, blank=True)

class Reply (models.Model):
    writer=models.CharField(max_length=20)
    content=models.TextField('내용')
    created_at=models.DateTimeField('작성일', null=True) 
    #이렇게 클래스 정의 후 migration 해주고 admin.py에 임포트해줌
    post=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='작성자', null=True, blank=True)

class Comment(models.Model):
    content=models.TextField(verbose_name='내용')
    created_at=models.DateTimeField('작성일', null=True) 
    post=models.ForeignKey(to='Post',on_delete=models.CASCADE,verbose_name='게시글')
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE,verbose_name='작성자',null=True)