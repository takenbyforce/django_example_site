from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import ProjectEntry, WebhookConfig
from .serializers import ProjectSerializer, WebhookSerializer
from .tasks import invoke_all_webhooks


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return hasattr(obj, 'owner') and request.user.id == obj.owner_id


class BasePermissionViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            permission_classes = [IsAuthenticated & IsObjectOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProjectEntryViewSet(BasePermissionViewSet):
    queryset = ProjectEntry.objects.all().order_by('id')
    serializer_class = ProjectSerializer

    def perform_create(self, serializer) -> None:
        data = serializer.save()
        invoke_all_webhooks.apply_async(args=(data.pk,))


class WebhookConfigViewSet(BasePermissionViewSet):
    queryset = WebhookConfig.objects.all().order_by('id')
    serializer_class = WebhookSerializer
