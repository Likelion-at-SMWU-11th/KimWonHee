from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, JsonResponse

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostBasedForm, PostCreateForm, PostDetailForm, PostUpdateForm
from rest_framework.viewsets import ModelViewSet

from .serializers import PostModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    return render(request, "index.html")


def post_list_view(request):
    # post_list=Post.objects.all() #post 모델에 있는 객체 전부 불러오기
    post_list = Post.objects.filter(
        writer=request.user
    )  # Post.writer가 현재 로그인 사용자인 데이터 조회
    context = {  # post 객체를 리스트 형태로 담기
        "post_list": post_list,
    }
    return render(request, "posts/post_list.html", context)


def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:  # 존재하지 않는 게시글을 조회할 경우
        return redirect("index")
    post = Post.objects.get(id=id)
    context = {
        "post": post,
        "form": PostDetailForm(),
    }
    return render(request, "posts/post_detail.html", context)


# 데코레이터 임포트..
@login_required
def post_create_view(request):
    if request.method == "GET":
        return render(request, "posts/post_form.html")
    else:
        #image = request.FILES.get("image")
        content = request.POST.get("content")
        Post.objects.create(  # image, content 데이터를 담은 Post 객체 만들어서 저장
            image=image, content=content, writer=request.user
        )
        return redirect("index")


@login_required
def post_update_view(request, id):  # url패턴에 id를 적었기 때문에 id가 올 수 있음.
    # post = Post.objects.get(id=id) #얘는 500에러가 뜸(쪼금 위험)
    # post = get_object_or_404(Post, id=id)  # 위 코드와 동일한 기능+ 유효하지 않은 id의 경우 자동으로 404를 띄워줌(조금 안전)
    post = get_object_or_404(Post, id=id, writer=request.user)  # 예외처리ver
    if request.method == "GET":
        context = {"post": post}
        return render(request, "posts/post_form.html", context)
    elif request.method == "POST":
        new_image = request.FILES.get("image")
        content = request.POST.get("content")

        if new_image:
            post.image.delete()
            post.image = new_image
        post.content = content
        post.save()

        return redirect("posts:post-detail", post.id)


@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    # 여기톤 때 url 숫자만 바꾸면 다른 사람 마이페이지로 들어가지던 오류 해소하는 방법 2가지
    # 1) post = get_object_or_404(Post, id=id, writer=request.user) <=가능한 이유: post모델에 writer필드가 있음
    # 2) 아래 두 줄의 코드 (일종의 예외처리!)
    if request.user != post.writer:
        raise Http404("잘못된 접근입니다.")

    if request.method == "GET":
        context = {"post": post}
        return render(
            request, "posts/post_confirm_delete.html", context
        )  # -> post_confirm_delete.html가 받음
    else:
        post.delete()
        return redirect("index")


class class_view(ListView):
    model = Post
    template_name = "cbv_view.html"


def url_view(request):
    data = {"code": "001", "msg": "OK"}
    return HttpResponse("<h1>url_views</h1>")


def url_parameter_view(request, username):
    print(f"url_parameter_view()")
    print(f"username: {username}")
    print(f"request.GET: {request.GET}")
    return HttpResponse(username)


def function_view(request):
    print(f"request.method: {request.method}")

    if request.method == "GET":
        print(f"request.GET: {request.GET}")
    elif request.method == "POST":
        print(f"request.POST: {request.POST}")
    return render(request, "view.html")


def index(request):  # post.objects.all(): post 모델에 있는 객체 전부 불러오기
    post_list = Post.objects.all().order_by(
        "-created_at"
    )  # order_by('created_at'): 오름차순, order_by('-created_at'): 내림차순 이런거.
    context = {
        "post_list": post_list,
    }
    return render(request, "index.html", context)


def post_create_form_view(request):
    if request.method == "GET":
        form = PostCreateForm()
        context = {"form": form}
        return render(request, "posts/post_form2.html", context)
    else:
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(  # image, content 데이터를 담은 post 객체 만들어서 저장
                image=form.cleaned_data["image"],
                content=form.cleaned_data["content"],
                writer=request.user,
            )
        else:
            return redirect("post:post-create")
        return redirect("index")
        # image = request.FILES.get("image")
        # content = request.POST.get("content")
        # Post.objects.create(  # image, content 데이터를 담은 Post 객체 만들어서 저장
        #     image=image, content=content, writer=request.user
        # )
        return redirect("index")

class PostModelViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostModelSerializer

@api_view()
def calculator(request):
    num1=request.GET.get('num1',0)
    num2=request.GET.get('num2',0)
    operators=request.GET.get('operators')

    if operators=='^':
        result=int(num1)+int(num2)
    elif operators=='-':
        result=int(num1)-int(num2)
    elif operators=='*':
        result=int(num1)*int(num2)
    elif operators=='/':
        result=int(num1)/int(num2)
    else:
        result=0
    data={
        'type':'FBW',
        'result':result
    }
    return Response(data)