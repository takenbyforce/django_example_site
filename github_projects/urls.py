from django.urls import include, path
from rest_framework import routers
from github_projects import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectEntryViewSet)
router.register('webhooks', views.WebhookConfigViewSet)

app_name = 'github_projects'
urlpatterns = [
    path('', include(router.urls)),
]
