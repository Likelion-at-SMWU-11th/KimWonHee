# settings.py의 BASE_DIR : 폴더 두 번 이동 정도는 봐주겠다. (앱 단위-> 프로젝트 단위로 범위가 확장됨)

from django.urls import path
from .views import post_list_view, post_create_view
from .views import post_delete_view, post_detail_view

app_name = "posts"  # post로 시작하는 애들만 남겨둔거.

urlpatterns = [
    path("", post_list_view, name="post-list"),
    path("new/", post_create_view),
    path("<int:id>/", post_detail_view),
    path("<int:id>/delete", post_delete_view),
]
