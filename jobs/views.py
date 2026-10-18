from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Job
from applications.models import Application

def job_list(request):

    jobs = Job.objects.all().order_by("-created_at")

    return render(request, "jobs/job_list.html", {
        "jobs": jobs
    })


@login_required
def create_job(request):
    if request.method == "POST":

        title = request.POST.get("title")
        company = request.POST.get("company")
        location = request.POST.get("location")
        description = request.POST.get("description")
        salary = request.POST.get("salary")
        job_type = request.POST.get("job_type")

        if not title or not company or not location or not description or not salary or not job_type:
            messages.error(request, "All fields are required.")
            return render(request,"jobs/create_job.html")

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            description=description,
            salary=salary,
            job_type=job_type,
            posted_by=request.user
        )

        messages.success(request, "Job posted successfully!")

        return redirect("job_list")
    return render(request, "jobs/create_job.html")


def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    application = None

    if request.user.is_authenticated:

        application = Application.objects.filter(
            job=job,
            applicant=request.user
        ).first()

    return render(request, "jobs/job_detail.html", {
        "job": job,
        "application": application
    })


@login_required
def edit_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if job.posted_by != request.user:
        messages.error(request, "You are not allowed to edit this job.")
        return redirect("job_list")

    if request.method == "POST":

        job.title = request.POST.get("title")
        job.company = request.POST.get("company")
        job.location = request.POST.get("location")
        job.description = request.POST.get("description")
        job.salary = request.POST.get("salary")
        job.job_type = request.POST.get("job_type")

        job.save()

        messages.success(request, "Job updated successfully!")

        return redirect("job_detail", job_id=job.id)

    return render(request, "jobs/edit_job.html", {
        "job" : job
    })

@login_required
def delete_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if job.posted_by != request.user:
        messages.error(request, "You are not allowed to delete this job.")
        return redirect("job_list")

    if request.method == "POST":
        job.delete()

        messages.success(request, "Job deleted successfully!")

        return redirect("job_list")

    return render(request, "jobs/delete_job.html", {
        "job": job
    })
# Create your views here.
