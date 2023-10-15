from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Passion, UserMedia, BodyType, Education, MaritalStatus, Gender, IdealMatch


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions",
         {"fields": (
             "is_staff", "is_active", "is_root_user", "is_team_member", "root_user", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)


class PassionAdmin(admin.ModelAdmin):
    list_display = ('id', 'passion', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(Passion, PassionAdmin)


class IdealMatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'ideal_match', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(IdealMatch, IdealMatchAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(Gender, GenderAdmin)


class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'marital_status', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(MaritalStatus, MaritalStatusAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'education', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(Education, EducationAdmin)


class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(BodyType, BodyTypeAdmin)


class UserMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


admin.site.register(UserMedia, UserMediaAdmin)
