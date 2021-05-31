from django.apps.config import AppConfig
from django.utils.translation import gettext_lazy as _l


class UsersConfig(AppConfig):
    name: str = "users"
    verbose_name: str = _l("Users")
