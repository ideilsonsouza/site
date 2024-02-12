from django.urls import path, include
from backend.request.api.views import test_view

app_name = 'backend.request.api'

urlpatterns = [
    path('/test/', test_view, name='test_api'),
]