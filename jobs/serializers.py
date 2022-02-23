from rest_framework import serializers
from jobs.models import Job, JobType


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id',
                  'value')


class JobSerializer(serializers.ModelSerializer):
    # Add job_type reference for each job
    job_type = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='value',
        queryset=JobType.objects.all()
    )

    class Meta:
        model = Job
        fields = ('id',
                  'title',
                  'job_type')
