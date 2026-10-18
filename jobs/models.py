from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    description = models.TextField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    job_type = models.CharField(max_length=100)

    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
