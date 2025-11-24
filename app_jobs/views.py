from django.shortcuts import render
from .models import Job
from django.db.models import Q
# Create your views here.
def Signupsucess(request):
    return render(request, 'Signupsucess.html')
def Signuperror(request):
    return render(request, 'Signuperror.html')
def Searchjobs(request):
    return render(request, "Searchjobs.html")


def search_jobs(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')
    experience = request.GET.get('experience', '')

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(company_name__icontains=query) |
            Q(job_title__icontains=query) |
            Q(job_category__icontains=query)
        )
    if location:
        jobs = jobs.filter(location__icontains=location)
    if experience:
        jobs = jobs.filter(experience_needed__icontains=experience)

    return render(request, '', {'jobs': jobs})