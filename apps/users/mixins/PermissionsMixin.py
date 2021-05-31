from django.contrib.auth.models import Group, Permission, PermissionsMixin as BasePermissionsMixin
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ManyToManyField
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _l

from users.models import User


class PermissionsMixin(BasePermissionsMixin):
    groups: ManyToManyField = ManyToManyField(
        Group,
        blank=True,
        help_text=_l(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name=_l("groups"),
    )
    is_superuser: BooleanField = BooleanField(
        _l("is superuser"),
        default=False,
        help_text=_l(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    permissions: ManyToManyField = ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text=_l("Specific permissions for this user."),
        verbose_name=_l("permissions"),
    )

    class Meta:
        abstract: bool = True

    @property
    def user_permissions(self) -> None:
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'user_permissions'")

    def _get_user_permissions(self, user: User) -> QuerySet[Permission]:
        return getattr(user, "permissions").all()
