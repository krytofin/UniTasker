from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

import json

class Subject(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Homework(models.Model):
    STATUS = (
            ('t', 'todo'),
            ('p', 'in_progress'),
            ('d', 'done'),
    )


    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(choices=STATUS, max_length=1, default='t')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return f'{self.subject.title}: {self.title}, {self.deadline}'

    def is_burning(self):
        delta = self.deadline - timezone.now().date()
        return 0 <= delta.total_seconds() / 3600 < 24

    def as_object(self):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description or "",
            "subject": self.subject.title,
            "professor": self.subject.professor or "",
            "status_raw": self.status,
            "status_display": self.get_status_display(),
            "deadline": self.deadline.strftime("%b %d, %Y %H:%M"),
            "is_burning": self.is_burning(), 
            "update_url": reverse("diary:update_homework", args=[self.pk]) 
        }
        return json.dumps(data, ensure_ascii=False)
