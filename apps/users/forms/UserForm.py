from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput
from django.utils.translation import gettext as _, gettext_lazy as _l

from users.models import User


class UserForm(ModelForm):
    confirm_password: CharField = CharField(
        help_text=_l("Enter the same password as above, for verification."),
        label=_l("Confirm password"),
        required=False,
        strip=False,
        widget=PasswordInput
    )
    password: CharField = CharField(label=_l("Password"), required=False, strip=False, widget=PasswordInput)

    class Meta:
        fields: str = "__all__"
        model: type = User

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.instance:
            self._meta.fields = ("phone", "password", "confirm_password")
        if permissions := self.fields.get("permissions"):
            permissions.queryset = permissions.queryset.select_related("content_type")

    def clean_password(self):
        confirm_password: str = self.cleaned_data.get("confirm_password")
        password: str = self.cleaned_data.get("password")
        if confirm_password and password:
            if confirm_password != password:
                raise ValidationError(_("Passwords don't match."))
            self.instance.set_password(password)
        return password
