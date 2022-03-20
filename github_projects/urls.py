from django.urls import include, path
from rest_framework import routers
from github_projects import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
