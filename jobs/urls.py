from django.urls import path
from .views import edit_job, job_list,create_job, job_detail, delete_job

urlpatterns = [
    path("", job_list, name="job_list"),
    path("create/", create_job, name="create_job"),
    path("<int:job_id>/", job_detail, name="job_detail"),
    path("<int:job_id>/edit/", edit_job, name="edit_job"),
    path(
    "<int:job_id>/delete/",
    delete_job,
    name="delete_job"
),
]