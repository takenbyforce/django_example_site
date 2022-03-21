from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=True)),
    path('api/', include('github_projects.urls')),
    path('admin/', admin.site.urls),
]
