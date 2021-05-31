from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _l

from utils.functional import upload_to


class Photo(Model):
    created_at: DateTimeField = DateTimeField(_l("created at"), auto_now_add=True)
    file: ImageField = ImageField(_l("file"), upload_to=upload_to)
    user: ForeignKey = ForeignKey("users.User", CASCADE, "photo_set", verbose_name=_l("user"))

    class Meta:
        db_table: str = "photos"
        ordering: tuple = ("-created_at",)
        verbose_name: str = _l("photo")
        verbose_name_plural: str = _l("photos")

    def __str__(self) -> str:
        return self.created_at.strftime("%d.%m.%Y at %H:%M")

    @property
    def file_directory(self) -> str:
        return f"users/{self.user.pk}/photos/"
