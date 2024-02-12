from django.urls import path, include
from backend.request.web.views import accessible_page, HomeView, DownloadsView

app_name = 'backend.request.web'

urlpatterns = [
    path('test/', accessible_page, name='page_test'),
    path('', HomeView.as_view(), name='home'),
    path('downloads/', DownloadsView.as_view(), name='downloads')
]