from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__' #모든 필드가 다 나옴. (id, image, content, created_at, view_count, writer)
        #fields=['id', 'writer', 'content'] #세 필드만 나옴. 

class PostListSerializer(PostModelSerializer): #저번 시간에 만든 postmodelserializer를 상속받음. 
    class Meta(PostModelSerializer.Meta):
        fields=['id',
                'image',
                'content',
                'writer',                
                'created_at',
                'view_count',
                ]
        depth=1

#게시판(글)을 생성하는 시리얼라이저
class PostCreateSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields=[
            'image',
            'content',
        ]

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer):
        depth=1

class commentListModelSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'