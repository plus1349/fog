from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.deletion import SET_NULL
from django.db.models.fields import BooleanField, CharField, DateTimeField, TextField
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _l

from users.managers import UserManager, objects
from users.mixins import PermissionsMixin
from users.models.fields import PhoneField, UsernameField


class User(AbstractBaseUser, PermissionsMixin):
    bio: TextField = TextField(_l("bio"), blank=True, max_length=70, null=True)
    date_joined: DateTimeField = DateTimeField(_l("date joined"), auto_now_add=True)
    is_active: BooleanField = BooleanField(_l("is active"), default=True)
    is_staff: BooleanField = BooleanField(_l("is staff"), default=False)
    name: CharField = CharField(_l("name"), blank=True, max_length=128, null=True)
    phone: PhoneField = PhoneField(_l("phone"), max_length=16, unique=True)
    photo: OneToOneField = OneToOneField("users.Photo", SET_NULL, blank=True, null=True, related_name="user+")
    username: UsernameField = UsernameField(_l("username"), blank=True, max_length=32, null=True, unique=True)

    objects: UserManager = objects

    REQUIRED_FIELDS: tuple = ()
    USERNAME_FIELD: str = "phone"

    class Meta:
        db_table: str = "users"
        verbose_name: str = _l("user")
        verbose_name_plural: str = _l("users")

    def __str__(self) -> str:
        return f"{self.name or self.username or self.phone}"

    def save(self, *args, **kwargs) -> None:
        if not self.password:
            self.set_unusable_password()
        super().save(*args, **kwargs)
