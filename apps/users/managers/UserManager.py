from django.contrib.auth.base_user import BaseUserManager

from users.models import User


class UserManager(BaseUserManager):
    use_in_migrations: bool = True

    def _create_user(self, phone: str, password: str, **fields) -> User:
        user: User = self.model(phone=phone, **fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone: str, password: str, **fields) -> User:
        fields.setdefault("is_staff", True)
        fields.setdefault("is_superuser", True)
        return self._create_user(phone, password, **fields)


objects = UserManager()
