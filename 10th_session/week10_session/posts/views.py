from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    #post_list=Post.objects.all() #post 모델에 있는 객체 전부 불러오기
    post_list=Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인 사용자인 데이터 조회
    context={ #post 객체를 리스트 형태로 담기
        'post_list':post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExist: #존재하지 않는 게시글을 조회할 경우
        return redirect('index')
    post=Post.objects.get(id=id)
    context={
        'post':post, 
    }
    return render(request, 'posts/post_detail.html', context)

#데코레이터 임포트
@login_required
def post_create_view(request):
    if request.method=="GET":
        return render(request, 'posts/post_form.html')
    else:
        image=request.FILES.get('image')
        content=request.POST.get('content')
        Post.objects.create( #image, content 데이터를 담은 Post 객체 만들어서 저장
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index')

def post_update_view(request, id):
    return render(request, 'posts/post_update.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

def url_view(request):
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_views</h1>')

def url_parameter_view(request, username):
    print(f'url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

def index(request): #post.objects.all(): post 모델에 있는 객체 전부 불러오기
    post_list=Post.objects.all().order_by('-created_at') #order_by('created_at'): 오름차순, order_by('-created_at'): 내림차순 이런거. 
    context={
        'post_list':post_list,
    }
    return render(request, 'index.html', context)