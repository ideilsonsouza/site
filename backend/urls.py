from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('system/admin/', admin.site.urls),
    path('',include('backend.request.web.urls')),
    path('api/', include('backend.request.api.urls')),
]
