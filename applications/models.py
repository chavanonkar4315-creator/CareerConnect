from django.db import models

from django.contrib.auth.models import User
from jobs.models import Job

class Application(models.Model):

    STATUS_CHOICE = [
        ("pending", "Pending"),
        ("shortlisted", "Shortlisted"),
        ("rejected", "Rejected")
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    cover_letter = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default="pending"
    )

    applied_at = models.DateTimeField(
        auto_now_add=True

    )

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
# Create your models here.
