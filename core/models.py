from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.todo
    class Meta:
        ordering = ('-created_at',)
