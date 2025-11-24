from django.db import models
from app_users.models import User
# Create your models here.

class Job(models.Model):
    class JobTypeChoices(models.TextChoices):
        FULL_TIME = 'Full-Time'
        PART_TIME = 'Part-Time'
        INTERNSHIP = 'Internship'
        CONTRACT = 'Contract'

    job_id = models.AutoField(primary_key=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'usertype': 'Recruiter'})
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_category = models.CharField(max_length=100, db_index=True)
    job_type = models.CharField(max_length=20, choices=JobTypeChoices.choices)
    job_description = models.TextField()
    experience_needed = models.CharField(max_length=100)

    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)

    posted_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        ordering = ['-posted_date']
        verbose_name_plural = 'Jobs'

