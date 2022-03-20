from rest_framework import serializers

from .models import ProjectEntry


class ProjectEntrySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = ProjectEntry
        fields = '__all__'
