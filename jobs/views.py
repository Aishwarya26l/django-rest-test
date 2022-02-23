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
