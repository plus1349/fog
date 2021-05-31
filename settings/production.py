from settings.base import *


DEBUG: bool = False

STATIC_ROOT: Union[PosixPath, WindowsPath] = ROOT_DIR / "static"
