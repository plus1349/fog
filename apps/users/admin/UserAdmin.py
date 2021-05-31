from django.contrib.admin.decorators import register
from django.contrib.admin.options import TabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.core.handlers.wsgi import WSGIRequest
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _, gettext_lazy as _l

from utils.decorators import short_description

from users.forms import UserForm
from users.models import Photo, User


class PhotoInlineAdmin(TabularInline):
    classes: tuple = ("collapse",)
    extra: int = 0
    model: type = Photo


@register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets: tuple = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password", "confirm_password")
        }),
    )
    add_form: type = UserForm
    change_password_form: type = AdminPasswordChangeForm
    date_hierarchy: str = "date_joined"
    fieldsets: tuple = (
        (None, {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_l("AUTHENTICATION"), {"fields": ("phone", "change_password")}),
        (_l("GROUPS"), {"fields": ("groups",)}),
        (_l("PERMISSIONS"), {"fields": ("permissions",)}),
        (_l("INFORMATION"), {"fields": ("photo", "username", "name", "bio", "last_login", "date_joined")}),
    )
    filter_horizontal: tuple = ('groups', 'permissions')
    form: type = UserForm
    inlines: tuple = (PhotoInlineAdmin,)
    list_display: tuple = ("id", "is_active", "is_staff", "is_superuser", "phone", "date_joined")
    list_display_links: tuple = ("phone",)
    list_editable: tuple = ("is_active",)
    list_filter: tuple = ("is_active", "is_staff", "is_superuser")
    ordering: tuple = ("id",)
    readonly_fields: tuple = ("date_joined", "last_login", "change_password")
    search_fields: tuple = ("phone",)

    @mark_safe
    @short_description(_("Password"))
    def change_password(self, instance: User) -> str:
        return _("You can change the password using <a href=\"../password/\">this form</a>")

    def get_inlines(self, request: WSGIRequest, instance: User) -> list:
        return super().get_inlines(request, instance) if instance else super().inlines
