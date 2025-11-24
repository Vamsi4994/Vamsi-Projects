from django.db import models
from app_jobs.models import Job
from app_users.models import User
# Create your models here.

class JobApplication(models.Model):
    class StatusChoices(models.TextChoices):
        APPLIED = 'Applied'
        SHORTLISTED = 'Shortlisted'
        REJECTED = 'Rejected'
        SELECTED = 'Selected'

    application_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'usertype': 'Job_Seeker'})
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.APPLIED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_seeker.first_name} applied to {self.job.job_title} ({self.status})"

    class Meta:
        ordering = ['-application_date']
        verbose_name_plural = 'Job Applications'
