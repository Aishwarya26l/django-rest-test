from django.conf.urls import url
from jobs.views import JobList

urlpatterns = [
    url(r'^jobs$', JobList.as_view()),
]
