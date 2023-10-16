import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class FilePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to="file/post/", blank=True, null=True)
    text = models.TextField(default=None, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def total_likes(self):
        return LikeFilePost.objects.filter(file_post=self).count()

    @property
    def total_share(self):
        return ShareFilePost.objects.filter(file_post=self).count()

    @property
    def total_views(self):
        return ViewFilePost.objects.filter(file_post=self).count()

    @property
    def total_comments(self):
        return CommentFilePost.objects.filter(file_post=self).count()


class ViewFilePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    file_post = models.ForeignKey(FilePost, on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'file_post')


class LikeFilePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    file_post = models.ForeignKey(FilePost, on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'file_post')


class ShareFilePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    file_post = models.ForeignKey(FilePost, on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CommentFilePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    file_post = models.ForeignKey(FilePost, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    text = models.TextField(default=None, blank=True, null=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-create_at',)
    @property
    def total_replies(self):
        return CommentFilePost.objects.filter(parent_comment=self).count()
