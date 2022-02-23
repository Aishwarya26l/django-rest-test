from rest_framework import serializers
from jobs.models import Job, JobType


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id',
                  'value')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id',
                  'title',
                  'job_type')
