from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr_dashboard/', include('hr_dashboard.urls')),
    path('role_customization/', include('role_customization.urls')),
]
