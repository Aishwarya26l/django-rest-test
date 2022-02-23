from django.http import Http404
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class JobList(APIView):
    """
    List all jobs, or create a new job.
    """

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return Job.objects.all()

    def get(self, request, format=None):
        snippets = self.get_queryset()
        serializer = JobSerializer(snippets, many=True)
        return Response(serializer.data)

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

    def get_queryset(self):
        return Job.objects.all()

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
