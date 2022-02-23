from django.urls import path
from jobs.views import JobList, JobDetail

urlpatterns = [
    path('jobs/', JobList.as_view()),
    path('jobs/<uuid:pk>', JobDetail.as_view()),
]
