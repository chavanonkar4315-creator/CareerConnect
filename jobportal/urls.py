from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return redirect("job_list")

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/", include("accounts.urls")),

    path("jobs/", include("jobs.urls")),

    path("applications/", include("applications.urls")),

    path("", home, name="home"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)