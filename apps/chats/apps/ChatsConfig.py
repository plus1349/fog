from django.apps.config import AppConfig
from django.utils.translation import gettext_lazy as _l


class ChatsConfig(AppConfig):
    name: str = "chats"
    verbose_name: str = _l("Chats")
