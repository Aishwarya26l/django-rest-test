from django.http import Http404
from jobs.models import Job, JobType
from jobs.serializers import JobSerializer, JobTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

job_param = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['title', 'job_type'],
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, example='Test Title'),
        'job_type': openapi.Schema(type=openapi.TYPE_STRING, example="Full time"),
        'description': openapi.Schema(type=openapi.TYPE_STRING, example='Description'),
        'salary_to': openapi.Schema(type=openapi.TYPE_NUMBER, example=100000),
        'salary_from': openapi.Schema(type=openapi.TYPE_NUMBER, example=50000),
    }
)


class JobList(APIView):
    """
    List all jobs, or create a new job.
    """

    authentication_classes = []
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        try:
            if('pk' in kwargs):
                return Job.objects.get(self.kwargs.get('pk'))
            else:
                return Job.objects.all()
        except Job.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={200: JobSerializer(many=True)}, operation_description="List all jobs")
    def get(self, request, format=None):
        jobs = self.get_queryset()

        # Paginate response
        paginator = PageNumberPagination()
        paginator.page_size = 5
        jobs_page = paginator.paginate_queryset(jobs, request)

        serializer = JobSerializer(jobs_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=job_param, operation_description="Create a new job")
    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetail(APIView):
    """
    Retrieve, update or delete a job instance.
    """

    authentication_classes = []
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        try:
            if('pk' in kwargs):
                return Job.objects.get(pk=self.kwargs.get('pk'))
            else:
                return Job.objects.all()
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_queryset(pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    @ swagger_auto_schema(request_body=job_param)
    def put(self, request, pk, format=None):
        job = self.get_queryset(pk=pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_queryset(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobTypeList(APIView):
    """
    List all job types
    """
    authentication_classes = []
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        try:
            if('pk' in kwargs):
                return Job.objects.get(self.kwargs.get('pk'))
            else:
                return Job.objects.all()
        except Job.DoesNotExist:
            raise Http404

    @ swagger_auto_schema(responses={200: JobTypeSerializer(many=True)})
    def get(self, request, format=None):
        jobTypes = self.get_queryset()

        # Paginate response
        paginator = PageNumberPagination()
        paginator.page_size = 5
        jobTypes_page = paginator.paginate_queryset(jobTypes, request)

        serializer = JobTypeSerializer(jobTypes_page, many=True)
        return paginator.get_paginated_response(serializer.data)
