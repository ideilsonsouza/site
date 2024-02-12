from django.apps import AppConfig
from django.conf import settings

APPS_REST_FRAMEWORK = [
    'rest_framework',
    'rest_framework.authtoken',
]

for app in APPS_REST_FRAMEWORK:
    if app and app not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS.append(app)

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.request.api'
