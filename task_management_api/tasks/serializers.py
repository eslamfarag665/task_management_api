from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority_level', 'status', 'user', 'created_at', 'updated_at']

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def validate_priority_level(self, value):
        if value not in dict(Task.PRIORITY_CHOICES):
            raise serializers.ValidationError("Invalid priority level.")
        return value

    def validate_status(self, value):
        if value not in dict(Task.STATUS_CHOICES):
            raise serializers.ValidationError("Invalid status.")
        return value
