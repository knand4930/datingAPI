from rest_framework import serializers
from .models import FilePost, ViewFilePost, LikeFilePost, ShareFilePost, CommentFilePost


class ViewFilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewFilePost
        fields = '__all__'


class LikeFilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeFilePost
        fields = '__all__'


class ShareFilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareFilePost
        fields = "__all__"


class CommentFilePostSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = CommentFilePost
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.first_name + obj.user.last_name if obj.user else "Anonymous"

    def get_replies(self, obj):
        replies = CommentFilePost.objects.filter(parent_comment=obj)
        return CommentFilePostSerializer(replies, many=True).data


class FilePostSerializer(serializers.ModelSerializer):
    total_views = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_share = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    liked_by = serializers.SerializerMethodField()
    viewed_by = serializers.SerializerMethodField()
    shared_by = serializers.SerializerMethodField()
    comments = CommentFilePostSerializer(many=True)

    class Meta:
        model = FilePost
        fields = '__all__'

    def get_total_likes(self, obj):
        return LikeFilePost.objects.filter(file_post=obj).count()

    def get_total_views(self, obj):
        return ViewFilePost.objects.filter(file_post=obj).count()

    def get_total_comments(self, obj):
        return obj.total_comments

    def get_total_share(self, obj):
        return ShareFilePost.objects.filter(file_post=obj).count()
    def get_liked_by(self, obj):
        liked_users = LikeFilePost.objects.filter(file_post=obj).values_list('user', flat=True)
        return liked_users


    def get_viewed_by(self, obj):
        viewed_users = ViewFilePost.objects.filter(file_post=obj).values_list('user', flat=True)
        return viewed_users

    def get_shared_by(self, obj):
        shared_users = ShareFilePost.objects.filter(file_post=obj).values_list('user', flat=True)
        return shared_users



    def get_comments(self, obj):
        comments = CommentFilePost.objects.filter(file_post=obj, parent_comment=None)
        return CommentFilePostSerializer(comments, many=True).data
