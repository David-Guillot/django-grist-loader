SECRET_KEY = "NOTASECRET"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = ["grist_loader", "tests"]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}]

ROOT_URLCONF = "tests.urls"

MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"]

SECURE_PROXY_SSL_HEADER = ("HTTP_FAKE_SECURE", "true")

USE_TZ = True

GRIST_PYGRISTER_CONFIG = {}
