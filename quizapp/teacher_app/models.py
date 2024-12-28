from django.db import models
from django.utils.crypto import get_random_string

class Class(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('student_app.StudentProfile', related_name="classes_enrolled")  # Lazy import
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='classes')
    join_code = models.CharField(max_length=10, blank=True, null=True)

    def generate_join_code(self):
        import random
        import string
        self.join_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.save()
            
    def __str__(self):
            return self.name
      

class Quiz(models.Model):
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    scheduled_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()  # Length of the quiz in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True/False'),
        ('ID', 'Identification'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
    correct_answer = models.TextField()  # Correct answer for auto-checking

    def __str__(self):
        return self.question_text
