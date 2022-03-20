from rest_framework import viewsets

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer


class ProjectEntryViewSet(viewsets.ModelViewSet):
    queryset = ProjectEntry.objects.all()
    serializer_class = ProjectEntrySerializer
