from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complaint(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Noticed", "Noticed"),
        ("Resolved", "Resolved"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.TextField()
    importance = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.complaint[:30]} ({self.status})"
    
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"To {self.user.username}: {self.message[:30]}..."

