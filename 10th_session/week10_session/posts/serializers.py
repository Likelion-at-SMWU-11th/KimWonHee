from rest_framework.serializers import ModelSerializer
from .models import Post

class PostModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        #fields='__all__' #모든 필드가 다 나옴. 
        fields=['id', 'writer', 'content'] #세 필드만 나옴. 