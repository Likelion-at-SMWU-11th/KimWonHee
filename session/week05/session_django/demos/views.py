from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 함수 작성-함수의 첫 번째 인자는 request라고 생각하고 작성!
def helloBabyLion(request):  # request 받아서
    # return HttpResponse("장고의 세계로 들어왔습니다.")
    # 이렇게 응답해 줄 것이다...
    return render(request, "crazyDjango.html")
    # view에게 우리가 만든 template(html 파일)을 사용하라고 알려주는 과정
