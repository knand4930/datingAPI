from django.shortcuts import render
from rest_framework.permissions import AllowAny

from posts.models import FilePost, ShareFilePost, CommentFilePost, LikeFilePost, ViewFilePost
from posts.serializers import (FilePostSerializer, ShareFilePostSerializer, CommentFilePostSerializer,
                               LikeFilePostSerializer, ViewFilePostSerializer)

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView


# Create your views here.

class FilePostListAPI(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = FilePostSerializer
    queryset = FilePost.objects.all()
