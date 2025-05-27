from django.db import models

class Flashcard(models.Model):
    student_id = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject}: {self.question[:50]}..."