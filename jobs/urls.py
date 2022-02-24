from django.urls import path
from jobs.views import JobList, JobDetail, JobTypeList

urlpatterns = [
    path('jobs/', JobList.as_view(), name="job_list"),
    path('jobs/<uuid:pk>', JobDetail.as_view(), name="job_detail"),
    path('job-types/', JobTypeList.as_view(), name="jobType_list")
]
