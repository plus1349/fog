from pathlib import Path, PosixPath
from sys import path

from django.utils.translation import gettext_lazy as _


ROOT_DIR: PosixPath = Path(__file__).resolve().parent.parent

path.append(str(ROOT_DIR / "apps"))
path.append(str(ROOT_DIR / "lib"))

SECRET_KEY: str = "secret"

DEBUG: bool = False

ALLOWED_HOSTS: list = ["*"]

INSTALLED_APPS: list = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE: list = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF: str = "urls"

TEMPLATES: list = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ROOT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
            ],
        },
    },
]

ASGI_APPLICATION: str = "asgi.application"
WSGI_APPLICATION: str = "wsgi.application"

DATABASES: dict = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "fog-backend.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS: list = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE: str = "en-us"
LANGUAGES: list = [
    ("en", _("English")),
    ("ru", _("Russian")),
]

LOCALE_PATHS: list = [ROOT_DIR / "locale"]

TIME_ZONE: str = "UTC"

USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True

FIXTURE_DIRS: list = [ROOT_DIR / "fixtures"]

Path(ROOT_DIR / "media").mkdir(exist_ok=True)
MEDIA_ROOT: PosixPath = ROOT_DIR / "media"
MEDIA_URL: str = "/media/"

Path(ROOT_DIR / "static").mkdir(exist_ok=True)
STATIC_ROOT: PosixPath = ROOT_DIR / "static"
STATIC_URL: str = "/static/"

Path(ROOT_DIR / "log" / "django" / "request").mkdir(exist_ok=True, parents=True)
Path(ROOT_DIR / "log" / "django" / "server").mkdir(exist_ok=True, parents=True)
LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.request": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\n[{server_time}] {message}",
            "style": "{",
        },
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "django.request": {
            "backupCount": 10240,
            "class": "logging.handlers.RotatingFileHandler",
            "encoding": "utf8",
            "filename": str(ROOT_DIR / "log/django/request/request.log"),
            "formatter": "django.request",
            "level": "ERROR",
            "maxBytes": 10485760,
        },
        "django.server": {
            "backupCount": 10240,
            "class": "logging.handlers.RotatingFileHandler",
            "encoding": "utf8",
            "filename": str(ROOT_DIR / "log/django/server/server.log"),
            "formatter": "django.server",
            "level": "INFO",
            "maxBytes": 10485760,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["django.request"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

try:
    from settings.dev import *
except ImportError:
    pass
else:
    del STATIC_ROOT
