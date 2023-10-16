from django.contrib import admin
from posts.models import FilePost, ViewFilePost, LikeFilePost, ShareFilePost, CommentFilePost


# Register your models here.

class FilePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_likes', 'total_share', 'total_views', 'total_comments')
    list_filter = ('create_at', 'update_at')


admin.site.register(FilePost, FilePostAdmin)


class ViewFilePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file_post')
    list_filter = ('create_at', "update_at")


admin.site.register(ViewFilePost, ViewFilePostAdmin)


class LikeFilePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file_post')
    list_filter = ('create_at', "update_at")


admin.site.register(LikeFilePost, LikeFilePostAdmin)


class ShareFilePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file_post')
    list_filter = ('create_at', "update_at")


admin.site.register(ShareFilePost, ShareFilePostAdmin)


class CommentFilePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file_post')
    list_filter = ('create_at', "update_at")


admin.site.register(CommentFilePost, CommentFilePostAdmin)
