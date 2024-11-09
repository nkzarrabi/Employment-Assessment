from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr_dashboard/', include('hr_dashboard.urls')),
    path('role_customization/', include('role_customization.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='react_app'),
]
