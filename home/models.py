from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)  # Task title
    time = models.TimeField()  # Time for the task
    is_completed = models.BooleanField(default=False)  # Status (completed or not)

    def __str__(self):
        return self.task_name
