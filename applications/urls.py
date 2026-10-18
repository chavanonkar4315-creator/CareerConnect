from django.urls import path
from .views import apply_job, job_applications, update_status, my_applications, employer_dashboard

urlpatterns = [
    path('apply/<int:job_id>/', apply_job, name='apply_job'),

    path(
        "<int:job_id>/applications/",
        job_applications,
        name="job_applications"
    ),

    path(
    "<int:application_id>/status/",
    update_status,
    name="update_status"
    ),

    path(
        "my-applications/",
        my_applications,
        name="my_applications"
    ),

    path(
    "employer-dashboard/",
    employer_dashboard,
    name="employer_dashboard"
    ),
]