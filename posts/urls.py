from django.urls import path

from posts.views import FilePostListAPI

urlpatterns = [
    path('get/', FilePostListAPI.as_view(), name="FilePostListAPI"),
]