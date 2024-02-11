from django.urls import path, include
from backend.request.web.views import accessible_page

app_name = 'backend.request.web'

urlpatterns = [
    path('/test', accessible_page, name='page_test')
]