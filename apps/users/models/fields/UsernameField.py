from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField

from users.validators import validate_username


class UsernameField(CharField):
    min_length: int = 5

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.validators.extend((MinLengthValidator(self.min_length), validate_username))
