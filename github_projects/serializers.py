from rest_framework import serializers

from .models import ProjectEntry, WebhookConfig


class BaseOwnerSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='owner.username', read_only=True)


class ProjectSerializer(BaseOwnerSerializer):
    class Meta:
        model = ProjectEntry
        fields = '__all__'


class WebhookSerializer(BaseOwnerSerializer):
    class Meta:
        model = WebhookConfig
        fields = '__all__'
