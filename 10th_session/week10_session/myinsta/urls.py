from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path("", include(router.urls)),    
    path("admin/", admin.site.urls),
    # Function Based View
    path("url/", url_view),
    path("url/<str:username>/", url_parameter_view),
    path("fbv/", function_view),
    # Class Based View
    path("cbv/", class_view.as_view()),  # as_view: 진입 메소드
    #path("", index, name="index"),
    path("posts/", include("posts.urls", namespace="posts")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("calculator/", calculator, name="calculator"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
