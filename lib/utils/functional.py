from pathlib import PurePath
from uuid import UUID, uuid4

from django.db.models.base import Model


def upload_to(instance: Model, filename: str) -> PurePath:
    file_directory: str = getattr(instance, "file_directory", "/")
    extension: str = PurePath(filename).suffix
    filename: UUID = uuid4()
    return PurePath(file_directory, f"{filename}{extension}")
