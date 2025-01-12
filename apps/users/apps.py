import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "apps.users"
    verbose_name = _("Foydalanuvchilar bo'limi")

    def ready(self):
        with contextlib.suppress(ImportError):
            import apps.users.signals  # noqa: F401
