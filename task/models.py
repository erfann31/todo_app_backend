from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('3', 'Low'),
        ('2', 'Medium'),
        ('1', 'High'),
        ('0', 'Not Specified')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    tag = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='0')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
