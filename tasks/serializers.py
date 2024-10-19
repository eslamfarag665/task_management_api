from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    completed_at = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 
            'priority_level', 'status', 'user', 
            'created_at', 'updated_at', 'completed_at'
        ]


    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The delivery date should be in the future.")
        return value

    def validate_priority_level(self, value):
        if value not in dict(Task.PRIORITY_CHOICES):
            raise serializers.ValidationError("The priority level is incorrect.")
        return value

    def validate_status(self, value):
        if value not in dict(Task.STATUS_CHOICES):
            raise serializers.ValidationError("The condition is incorrect.")
        return value
    
    def validate(self, data):
        if self.instance and self.instance.status == 'COMPLETED':
            if data.get('status', 'COMPLETED') == 'COMPLETED':
                if any(field in data for field in ['title', 'description', 'due_date', 'priority_level']):
                    raise serializers.ValidationError("Completed tasks cannot be modified unless they status are returned to 'Pending' .")
        return data
