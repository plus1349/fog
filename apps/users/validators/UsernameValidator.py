from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _l


class UsernameValidator(RegexValidator):
    """
    Ensures that 'username' value contains only ascii characters such as letters, numbers and
    underscores, doesn't starts with number or underscore, doesn't ends with underscore and
    doesn't have double underscore in it.
    """
    message: str = _l(
        "Username should only contains ascii characters such as letters, numbers and underscores. "
        "Should not starts with digit or underscore, ends with underscore or contain double underscore."
    )
    regex: str = r"^(?![0-9_]){1}([a-zA-Z0-9_](?!__)){5,32}(?!_){1}$"


validate_username: UsernameValidator = UsernameValidator()
