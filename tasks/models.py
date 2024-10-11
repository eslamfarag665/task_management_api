from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
User = get_user_model()

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError('Due date must be in the future.')

    def __str__(self):
        return self.title
    
    def mark_as_completed(self):
        self.status = 'COMPLETED'
        self.completed_at = timezone.now()
        self.save()

    def mark_as_pending(self):
        self.status = 'PENDING'
        self.completed_at = None
        self.save()