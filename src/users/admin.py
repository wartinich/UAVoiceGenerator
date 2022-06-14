from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from django.contrib import admin
from django.utils.html import mark_safe
from users.models import User


@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display = ['id', 'username', 'email', 'show_avatar']
    list_display_links = ['id', 'username', 'email']
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'avatar_image', 'birth_date', 'sex')}),
        ('Permission', {'fields': ('is_superuser', 'is_active', 'is_staff')})
    )

    #Show avatar_image at admin
    def show_avatar(self, obj):
        if obj.avatar_image:
            return mark_safe("<img src='{}' width='60' />".format(obj.avatar_image.url))
        return "None"

    show_avatar.__name__ = "Image"
