from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from .models import Application


@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if job.posted_by == request.user:
        messages.error(request, "You cannot apply to your own job.")
        return redirect("job_detail", job_id=job.id)

    if Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists():

        messages.error(request, "You have already applied for this job.")
        return redirect("job_detail", job_id=job.id)

    if request.method == "POST":

        cover_letter = request.POST.get("cover_letter")

        resume = request.FILES.get("resume")

        Application.objects.create(
           job=job,
           applicant=request.user,
           cover_letter=cover_letter,
           resume=resume
)

        messages.success(
            request,
            "Application submitted successfully!"
        )

        return redirect("job_detail", job_id=job.id)

    return render(request, "applications/apply_job.html", {
        "job": job
    })


@login_required
def job_applications(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if job.posted_by != request.user:
        messages.error(
            request,
            "You are not allowed to view these applications."
        )
        return redirect("job_list")

    applications = Application.objects.filter(
        job=job
    ).select_related("applicant")

    return render(request, "applications/job_applications.html", {
        "job": job,
        "applications": applications
    })


@login_required
def update_status(request, application_id):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    #only the job owner can change the status
    if application.job.posted_by != request.user:
        messages.error(
            request,
            "You are not allowed to update this application."
        )

        return redirect("jon_list")

    if request.method == "POST":

        status = request.POST.get("status")

        if status in dict(Application.STATUS_CHOICE):

            application.status = status
            application.save()

            messages.success(
                request,
                "Application status updated!"
            )

    return redirect(
        "job_applications",
        job_id=application.job.id
    )


@login_required
def my_applications(request):

    applications = Application.objects.filter(
        applicant=request.user
    ).select_related("job")

    return render(
        request,
        "applications/my_applications.html",
        {
            "applications": applications
        }
    )

@login_required
def employer_dashboard(request):

        jobs = Job.objects.filter(
            posted_by=request.user
        ).prefetch_related("application_set")

        return render(
            request,
            "applications/employer_dashboard.html",
            {
                "jobs": jobs
            }
        )