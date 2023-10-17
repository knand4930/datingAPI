from django.urls import path

from posts.views import FilePostListAPI, FilePostDestroyAPI, FilePostUpdateAPI, FilePostRetrieveAPI, FilePostPostAPI, \
    ShareFilePostListAPI, ShareFilePostPostAPI, ShareFilePostRetrieveAPI, ShareFilePostUpdateAPI, \
    ShareFilePostDestroyAPI, CommentFilePostListAPI, CommentFilePostPostAPI, CommentFilePostRetrieveAPI, \
    CommentFilePostUpdateAPI, CommentFilePostDestroyAPI, LikeFilePostListAPI, LikeFilePostPostAPI, \
    LikeFilePostRetrieveAPI, LikeFilePostUpdateAPI, LikeFilePostDestroyAPI, ViewFilePostListAPI, ViewFilePostPostAPI, \
    ViewFilePostRetrieveAPI, ViewFilePostUpdateAPI, ViewFilePostDestroyAPI, CommentRepliesView

urlpatterns = [
    path('get/', FilePostListAPI.as_view(), name="FilePostListAPI"),
    path('post/', FilePostPostAPI.as_view(), name="FilePostPostAPI"),
    path('<uuid:pk>/patch/', FilePostRetrieveAPI.as_view(), name="FilePostRetrieveAPI"),
    path('<uuid:pk>/update/', FilePostUpdateAPI.as_view(), name="FilePostUpdateAPI"),
    path('<uuid:pk>/delete/', FilePostDestroyAPI.as_view(), name="FilePostDestroyAPI"),

    path('share/get/', ShareFilePostListAPI.as_view(), name="ShareFilePostListAPI"),
    path('share/post/', ShareFilePostPostAPI.as_view(), name="ShareFilePostPostAPI"),
    path('share/<uuid:pk>/patch/', ShareFilePostRetrieveAPI.as_view(), name="ShareFilePostRetrieveAPI"),
    path('share/<uuid:pk>/update/', ShareFilePostUpdateAPI.as_view(), name="ShareFilePostUpdateAPI"),
    path('share/<uuid:pk>/delete/', ShareFilePostDestroyAPI.as_view(), name="ShareFilePostDestroyAPI"),

    path('comment/get/', CommentFilePostListAPI.as_view(), name="CommentFilePostListAPI"),
    path('comment/post/', CommentFilePostPostAPI.as_view(), name="CommentFilePostPostAPI"),
    path('comment/<uuid:pk>/patch/', CommentFilePostRetrieveAPI.as_view(), name="CommentFilePostRetrieveAPI"),
    path('comment/<uuid:pk>/update/', CommentFilePostUpdateAPI.as_view(), name="CommentFilePostUpdateAPI"),
    path('comment/<uuid:pk>/delete/', CommentFilePostDestroyAPI.as_view(), name="CommentFilePostDestroyAPI"),
    path('comments/replies/<uuid:parent_comment_id>/', CommentRepliesView.as_view(), name='comment-replies'),

    path('like/get/', LikeFilePostListAPI.as_view(), name="LikeFilePostListAPI"),
    path('like/post/', LikeFilePostPostAPI.as_view(), name="LikeFilePostPostAPI"),
    path('like/<uuid:pk>/patch/', LikeFilePostRetrieveAPI.as_view(), name="LikeFilePostRetrieveAPI"),
    path('like/<uuid:pk>/update/', LikeFilePostUpdateAPI.as_view(), name="LikeFilePostUpdateAPI"),
    path('like/<uuid:pk>/delete/', LikeFilePostDestroyAPI.as_view(), name="LikeFilePostDestroyAPI"),

    path('view/get/', ViewFilePostListAPI.as_view(), name="ViewFilePostListAPI"),
    path('view/post/', ViewFilePostPostAPI.as_view(), name="ViewFilePostPostAPI"),
    path('view/<uuid:pk>/patch/', ViewFilePostRetrieveAPI.as_view(), name="ViewFilePostRetrieveAPI"),
    path('view/<uuid:pk>/update/', ViewFilePostUpdateAPI.as_view(), name="ViewFilePostUpdateAPI"),
    path('view/<uuid:pk>/delete/', ViewFilePostDestroyAPI.as_view(), name="ViewFilePostDestroyAPI"),

]