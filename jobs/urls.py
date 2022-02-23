from django.urls import path
from jobs.views import JobList, JobDetail

urlpatterns = [
    path('jobs/', JobList.as_view(), name="job_list"),
    path('jobs/<uuid:pk>', JobDetail.as_view(), name="job_detail"),
]
