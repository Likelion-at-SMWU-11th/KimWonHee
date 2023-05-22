from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def NewDjangoProject(request):
    # return HttpResponse("장고의 세계로 들어왔습니다.")
    return render(request, "NewDjangoProject.html")
