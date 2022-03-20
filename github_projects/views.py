from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return hasattr(obj, 'owner') and request.user.id == obj.owner_id


class ProjectEntryViewSet(viewsets.ModelViewSet):
    queryset = ProjectEntry.objects.all().order_by('id')
    serializer_class = ProjectEntrySerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            permission_classes = [IsAuthenticated & IsObjectOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
