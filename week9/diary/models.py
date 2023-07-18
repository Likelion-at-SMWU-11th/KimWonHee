from django.db import models

# Create your models here.

class Diary (models.Model):
    image=models.ImageField(verbose_name='이미지')
    content=models.TextField('내용')
    created_at=models.DateTimeField('작성일')
    