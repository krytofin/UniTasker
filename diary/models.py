from django.db import models
from django.contrib.auth import get_user_model

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
    

    def __str__(self):
        return f'{self.subject.title}: {self.title}, {self.deadline}'
