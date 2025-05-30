"""
Running tests for django without using django-admin.py or using manage.py.

Basically run just by executing this file.

Thanks to:
    - http://stackoverflow.com/q/3841725/636136
    - http://stackoverflow.com/a/3851333/636136
    - http://stackoverflow.com/a/12260597/636136

"""

import django
from django.conf import settings
from django.core.management import call_command


def main() -> None:
    """Configures Django and runs the tests via Django."""
    settings.configure(
        MIDDLEWARE=(
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ),
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            }
        ],
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.admin",
            "django.contrib.messages",
            "django_markwhat",
        ),
    )

    django.setup()

    call_command("test", "-v3")


if __name__ == "__main__":
    main()
