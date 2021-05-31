from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _l


class PhoneValidator(RegexValidator):
    """Ensures that 'phone' startswith '+' and up to 15 digits."""
    message: str = _l("Phone number should starts with \"+\" and up to 16 digits.")
    regex: str = r"^\+?1?\d{9,15}$"


validate_phone: PhoneValidator = PhoneValidator()
