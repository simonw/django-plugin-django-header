import djp

SECRET_KEY = "django-insecure-test-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = []

MIDDLEWARE = []

ROOT_URLCONF = "tests.test_project.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_TZ = True

djp.settings(globals())
