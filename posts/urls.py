from django.urls import path

from posts.views import FilePostListAPI, FilePostDestroyAPI, FilePostUpdateAPI, FilePostRetrieveAPI, FilePostPostAPI

urlpatterns = [
    path('get/', FilePostListAPI.as_view(), name="FilePostListAPI"),
    path('post/', FilePostPostAPI.as_view(), name="FilePostPostAPI"),
    path('<uuid:pk>/patch/', FilePostRetrieveAPI.as_view(), name="FilePostRetrieveAPI"),
    path('<uuid:pk>/update/', FilePostUpdateAPI.as_view(), name="FilePostUpdateAPI"),
    path('<uuid:pk>/delete/', FilePostDestroyAPI.as_view(), name="FilePostDestroyAPI"),
]