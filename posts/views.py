from rest_framework import permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from posts.models import FilePost, ShareFilePost, CommentFilePost, LikeFilePost, ViewFilePost
from posts.serializers import (FilePostSerializer, ShareFilePostSerializer, CommentFilePostSerializer,
                               LikeFilePostSerializer, ViewFilePostSerializer, FilePostDataSerializer,
                               FilePostUpdateSerializer)
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListCreateAPIView


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


class ShareFilePostPostAPI(ListCreateAPIView):
    serializer_class = ShareFilePostSerializer
    queryset = ShareFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ShareFilePostListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShareFilePostSerializer
    queryset = ShareFilePost.objects.all()


class ShareFilePostRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShareFilePostSerializer
    queryset = ShareFilePost.objects.all()


class ShareFilePostUpdateAPI(UpdateAPIView):
    serializer_class = ShareFilePostSerializer
    queryset = ShareFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()

        if self.request.user == instance.user:
            serializer.save()
        else:
            return Response({"detail": "You do not have permission to update this object."},
                            status=status.HTTP_403_FORBIDDEN)


class ShareFilePostDestroyAPI(DestroyAPIView):
    serializer_class = ShareFilePostSerializer
    queryset = ShareFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "You do not have permission to delete this object."},
                            status=status.HTTP_403_FORBIDDEN)


class CommentFilePostPostAPI(ListCreateAPIView):
    serializer_class = CommentFilePostSerializer
    queryset = CommentFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CommentFilePostListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentFilePostSerializer
    queryset = CommentFilePost.objects.all()


class CommentFilePostRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentFilePostSerializer
    queryset = CommentFilePost.objects.all()


class CommentFilePostUpdateAPI(UpdateAPIView):
    serializer_class = CommentFilePostSerializer
    queryset = CommentFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()

        if self.request.user == instance.user:
            serializer.save()
        else:
            return Response({"detail": "You do not have permission to update this object."},
                            status=status.HTTP_403_FORBIDDEN)


class CommentFilePostDestroyAPI(DestroyAPIView):
    serializer_class = CommentFilePostSerializer
    queryset = CommentFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "You do not have permission to delete this object."},
                            status=status.HTTP_403_FORBIDDEN)


class LikeFilePostPostAPI(ListCreateAPIView):
    serializer_class = LikeFilePostSerializer
    queryset = LikeFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class LikeFilePostListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LikeFilePostSerializer
    queryset = LikeFilePost.objects.all()


class LikeFilePostRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LikeFilePostSerializer
    queryset = LikeFilePost.objects.all()


class LikeFilePostUpdateAPI(UpdateAPIView):
    serializer_class = LikeFilePostSerializer
    queryset = LikeFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()

        if self.request.user == instance.user:
            serializer.save()
        else:
            return Response({"detail": "You do not have permission to update this object."},
                            status=status.HTTP_403_FORBIDDEN)


class LikeFilePostDestroyAPI(DestroyAPIView):
    serializer_class = LikeFilePostSerializer
    queryset = LikeFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "You do not have permission to delete this object."},
                            status=status.HTTP_403_FORBIDDEN)


class ViewFilePostPostAPI(ListCreateAPIView):
    serializer_class = ViewFilePostSerializer
    queryset = ViewFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ViewFilePostListAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ViewFilePostSerializer
    queryset = ViewFilePost.objects.all()


class ViewFilePostRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ViewFilePostSerializer
    queryset = ViewFilePost.objects.all()


class ViewFilePostUpdateAPI(UpdateAPIView):
    serializer_class = ViewFilePostSerializer
    queryset = ViewFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()

        if self.request.user == instance.user:
            serializer.save()
        else:
            return Response({"detail": "You do not have permission to update this object."},
                            status=status.HTTP_403_FORBIDDEN)


class ViewFilePostDestroyAPI(DestroyAPIView):
    serializer_class = ViewFilePostSerializer
    queryset = ViewFilePost.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"detail": "You do not have permission to delete this object."},
                            status=status.HTTP_403_FORBIDDEN)


class CommentRepliesView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentFilePostSerializer

    def get_queryset(self):
        parent_comment_id = self.kwargs['parent_comment_id']
        return CommentFilePost.objects.filter(parent_comment_id=parent_comment_id)
