from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from posts.models import FilePost, ShareFilePost, CommentFilePost, LikeFilePost, ViewFilePost
from posts.serializers import (FilePostSerializer, ShareFilePostSerializer, CommentFilePostSerializer,
                               LikeFilePostSerializer, ViewFilePostSerializer, FilePostDataSerializer,
                               FilePostUpdateSerializer)

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
    ListCreateAPIView


# Create your views here.

class FilePostPostAPI(ListCreateAPIView):
    serializer_class = FilePostDataSerializer
    queryset = FilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class FilePostListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FilePostSerializer
    queryset = FilePost.objects.all()


class FilePostRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FilePostSerializer
    queryset = FilePost.objects.all()


class FilePostUpdateAPI(UpdateAPIView):
    serializer_class = FilePostUpdateSerializer
    queryset = FilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()

        if self.request.user == instance.user:
            serializer.save()
        else:
            return Response({"detail": "You do not have permission to update this object."},
                            status=status.HTTP_403_FORBIDDEN)


class FilePostDestroyAPI(DestroyAPIView):
    serializer_class = FilePostUpdateSerializer
    queryset = FilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "You do not have permission to delete this object."},
                            status=status.HTTP_403_FORBIDDEN)


