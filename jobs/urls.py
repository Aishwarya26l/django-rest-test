from django.urls import path
from jobs.views import JobList, JobDetail, JobTypeList

# Swagger intergration
# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Aishwarya - Jobs/Job types API",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here

urlpatterns = [
    path('doc/', schema_view.with_ui('swagger'),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'),
         name='schema-redoc'),
    path('jobs/', JobList.as_view(), name="job_list"),
    path('jobs/<uuid:pk>', JobDetail.as_view(), name="job_detail"),
    path('job-types/', JobTypeList.as_view(), name="jobType_list")
]
