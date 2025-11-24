from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'

    class UserTypeChoices(models.TextChoices):
        JOB_SEEKER = 'Job_Seeker'
        RECRUITER = 'Recruiter'
        EMPLOYEE = 'Employee'

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True, db_index=True)
    mobile_number = models.CharField(max_length=15)
    password=models.CharField(max_length=128)
    higher_education_degree = models.CharField(max_length=100)
    higher_education_branch = models.CharField(max_length=100)
    higher_education_year_of_passout = models.IntegerField()

    experience = models.PositiveIntegerField(help_text="Experience in years")

    location = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)

    usertype = models.CharField(max_length=20, choices=UserTypeChoices.choices)

    company_name = models.CharField(max_length=200, null=True, blank=True)
    company_address = models.TextField(null=True, blank=True)

    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.usertype})"

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name_plural = 'Users'
